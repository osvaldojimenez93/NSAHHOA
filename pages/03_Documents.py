import streamlit as st

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
## Governing Documents:
""")
st.download_button(
    label="Download Restrictive Covenants",
    data=covenant_bytes,
    file_name="Restrictive Covenants.pdf",
    mime="application/pdf"
)
st.download_button(
    label="Download ACC Renewal Document",
    data=acc_bytes,
    file_name="ACC Renewal Document.pdf",
    mime="application/pdf"
)

st.write("""
## 🏗️**Currently Working on Gathering all pertinent documents that would be helpful to residents.**🚧
""")