import streamlit as st
import streamlit.components.v1 as components

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

# st.header("HOA Documents")
st.write("""
## NSAH HOA Community Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/1yXwNi_VmXtBmoKjBofb7KftmJGDQebsX?usp=sharing")



st.write("""
## NSAH HOA Board Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/1UrXioC3CwTKg3OGYyd0MHuvVAdgt6auz?usp=drive_link")


