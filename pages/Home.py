import streamlit as st

pages = {
	"":[st.Page("Home.py", title="Home",),st.Page("AboutUs.py", title="About Us"), st.Page("Menu.py", title="Menu"), st.Page("Ingredients.py", title="Ingredients"), st.Page("Contact.py", title="Contact Us")]
}
st.navigation(pages, position="top").run()

