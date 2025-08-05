
import streamlit as st

# Replace with your new Vercel URL
new_url = "https://nsah-hoa.org/"

st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={new_url}" />
    If you are not redirected automatically, <a href="{new_url}">click here</a>.
""", unsafe_allow_html=True)



# Prevent indexing
st.markdown("""
    <meta name="robots" content="noindex">
""", unsafe_allow_html=True)
