import streamlit as st
import streamlit.components.v1 as components

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

# st.header("HOA Documents")
st.write("""
## NSAH HOA Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/16esqpVfBO-1Rj1e_bneNka6UfFXtZtUw?usp=sharing")


