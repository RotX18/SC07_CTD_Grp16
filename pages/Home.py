import streamlit as st
from upload_menu import db

st.title("AOMGOM Empire")
st.caption("Enjoy your-ghurt here :3")

menu = db.child("menu").get().val()

if not menu:
    st.error("Menu not available")
    st.stop()


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
    f"Choose sauces (up to {sauce_limit}", available_sauces, max_selections=sauce_limit
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

promotion = menu["sizes"][selected_size].get("promotion")
if promotion:
    st.info(f"Promotion: {promotion}")

if st.button("Place Order"):
    st.success("✅ Order placed! Thank you for your purchase.")
    # Optional: save order to Firebase
    order_data = {
        "size": selected_size,
        "flavour": selected_flavour,
        "toppings": selected_toppings,
        "sauces": selected_sauces
    }
    db.child("orders").push(order_data)