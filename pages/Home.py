import streamlit as st
import res.Utils as utils

utils.log("Home.py loaded.")

col1, col2 = st.columns(2, vertical_alignment="center", gap="large")

with col1:
	st.write("Crown Your Cup-",)
	st.header("Only at Aom Gom Empire !", anchor=False)

	#Order now button
	if st.button("Order Now!", key="OrderButton"):
		st.switch_page("./pages/Menu.py")
	st.markdown(
		"""
		<style>
			.st-key-OrderButton{
				width:9rem;
				height:3rem;
				border-radius: 50%;
			}
		</style>
		""", unsafe_allow_html=True
	)

with col2:
	st.markdown(
		"""
		<img class="homePic" src="https://static.wikitide.net/hellmetwiki/6/60/Panko.png">
		<style>
		.homePic{
			width: 100%;
			height: 100%;
			clip-path: circle(50%); !important
			overflow: hidden;
			object-fit:cover
		}
		</style>
		""", unsafe_allow_html=True
	)