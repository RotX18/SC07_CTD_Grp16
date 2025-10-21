import streamlit as st
import res.utils as utils


st.image("res/img/logo.png", width="stretch")

pages = {
    "": [
        st.Page("Home.py", title="Home"),
        st.Page("AboutUs.py", title="About Us"),
        st.Page("Menu.py", title="Menu"),
        st.Page("Ingredients.py", title="Ingredients")
    ]
}

st.navigation(pages, position="top").run()

utils.log('st.navigation(pages, position="top").run() executed successfully')