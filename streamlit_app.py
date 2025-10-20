import streamlit as st

pages = [
	 st.Page("./pages/Home.py", title = "Home"),
	 st.Page("./pages/AboutUs.py", title="About Us"), 
	 st.Page("./pages/Menu.py", title="Menu"),
	 st.Page("./pages/Ingredients.py", title="Ingredients"), 
	]

st.navigation(pages, position="top").run()
st.logo("./res/img/hi.jpg", size="large")