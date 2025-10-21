import streamlit as st
import res.utils as utils

utils.log("Ingredients.py loaded.")

col1, col2 = st.columns(2)

with col1:
	st.title("INGREDIENTS", anchor=False)
	st.markdown(
		"""
		All our yogurts and condiments are prepared with care and comfort. For you freshest experience, we ensure that our ingredients are prepared FRESHLY and HANDLED properly.

		**Core Ingredients**  
		We believe simple is best. Here are the core ingredients used across all our yogurt varieties:
		- **Milk**: Pasteurised, locally sourced milk
		- **Live & active cultures**: Beneficial bacteria (s. thermophilus and l.bulgarius) create our SIGNATURE tang and texture 
		"""
	)

with col2:
	st.markdown(
		"""
		<img class="homePic" src="https://pbs.twimg.com/media/FNmgEXNXMAowPKf.jpg:large">
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