import streamlit as st
import streamlit.components.v1 as components
from components.PageTemplate import render_page_template

render_page_template("HOA Documents")

st.write("""
## NSAH HOA Community Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/1yXwNi_VmXtBmoKjBofb7KftmJGDQebsX?usp=sharing")



st.write("""
## NSAH HOA Board Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/1UrXioC3CwTKg3OGYyd0MHuvVAdgt6auz?usp=drive_link")






