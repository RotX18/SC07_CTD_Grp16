import streamlit as st
import math
import res.Utils as utils

utils.log("Menu.py loaded.")

st.title("AOMGOM Empire")
st.caption("Enjoy your-ghurt here :3")

menu = utils.getMenu()

if not menu:
    st.error("Menu not available")
    st.stop()

# Student id
is_student = st.radio("Are you a student?", ("Yes", "No"))
if is_student == "Yes":
    student_id = st.text_input("Enter your student ID:")



sizes = list(menu["sizes"].keys())
selected_size = st.selectbox("Choose size", sizes)

flavours = [f for f, info in menu["flavours"].items() if info["available"]]
selected_flavour = st.selectbox("Choose flavour", flavours)

topping_limit = menu["sizes"][selected_size]["toppings_included"]
available_toppings = [t for t, info in menu["toppings"].items() if info["available"]]
selected_toppings = st.multiselect(
    f"Choose toppings (up to {topping_limit}, additional toppings + 0.5$ each))", available_toppings, max_selections=10
)

sauce_limit = menu["sizes"][selected_size]["sauces_included"]
available_sauces = [s for s, info in menu["sauces"].items() if info["available"]]
selected_sauces = st.multiselect(
    f"Choose sauces (up to {sauce_limit}", available_sauces, max_selections=sauce_limit,
)

st.markdown(
    """
    <style>
    .stMultiSelect{
        background-color: "White";
        text-color: "HotPink";
    }
    </style>
    """, unsafe_allow_html=True
)


# TOTAL PRICE CALCULATION
base_price = menu["sizes"][selected_size]["price"]
topping_price = 0.50 * max(0, len(selected_toppings) - topping_limit)
total = base_price + topping_price
st.metric("Total Price", f"${total:.2f}")


# ORDER SUMMARY SECTION
st.subheader("Order Summary")
st.write(f"Size: {selected_size.title()} — ${total:.2f}")
st.write(f"Flavour: {selected_flavour.title()}")
st.write(f"Toppings: {', '.join(selected_toppings) if selected_toppings else 'None'}")
st.write(f"Sauces: {', '.join(selected_sauces) if selected_sauces else 'None'}")

order = utils.Product(selected_size, total, student_id)
promotionSeason = order.applySeasonalDiscounts()
promotionStudent = order.applyStudentDiscount()

if promotionStudent:
    st.info("Valid Student ID✅ : 10% Student Discount applied ><")
afterDiscounted = order.discountedPrice
st.metric(label="Discounted Price ", value=f"${afterDiscounted:.2f}")

if st.button("Place Order"):
	st.success("Order placed! Thank you for your purchase.")
	utils.postOrderToDB(selected_size, selected_flavour, selected_toppings, selected_sauces)
	