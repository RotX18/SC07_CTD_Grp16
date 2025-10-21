import streamlit as st
import res.Utils as utils

utils.log("AboutUs.py loaded.")

col1, col2 = st.columns(2, vertical_alignment="center")
with col1:
	with st.container(horizontal_alignment="center"):
		st.title("About Us", anchor=False)
		st.markdown("""
		Born from a passion for bold flavours and a desire to shake up the yogurt scene, Aom Gom Empire is your HAPPY place. 
		We believe in high-quality ingredients, FRESH local pairings, and yogurt that makes you smile. 

		Our commitment is simple:  
		**Maximum flavour, maximum fun**

		**Grab your cup and join the empire!**

		""")
	with st.container(horizontal_alignment="center"):
		st.markdown(
			"""
			To reach out, 
			contact us at: aomgomempire@ctd.com OR  
			Call us at: 61234567
			"""
		)

with col2:
	st.image("res/img/logo.png", width="stretch")