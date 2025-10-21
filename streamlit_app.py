import streamlit as st

pages = [
	 st.Page("./pages/Home.py", title = "Home"),
	 st.Page("./pages/AboutUs.py", title="About Us"), 
	 st.Page("./pages/Menu.py", title="Menu"),
	 st.Page("./pages/Ingredients.py", title="Ingredients"), 
	]

st.navigation(pages, position="top").run()
st.logo("./res/img/logo.png", size="large")
st.markdown(
	"""
	<style>
		.stLogo{
			height: 6rem;
			width: auto;
		}
	</style>
	""", unsafe_allow_html=True
)