import streamlit as st
import streamlit.components.v1 as components

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

covenants = "documents/Restrictive Covenants.pdf"
with open(covenants, "rb") as f:
    covenant_bytes = f.read()
acc = "documents/ACC Renewal.pdf"
with open(acc, "rb") as f:
    acc_bytes = f.read()

# st.header("HOA Documents")
st.write("""
## NSAH HOA Documents:
""")
st.link_button("Go to Documents Drive", url="https://drive.google.com/drive/folders/16esqpVfBO-1Rj1e_bneNka6UfFXtZtUw?usp=sharing")


