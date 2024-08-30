import streamlit as st
import streamlit.components.v1 as components
from st_social_media_links import SocialMediaIcons

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

social_media_links = [
    "https://www.facebook.com/profile.php?id=61564446704590&mibextid=LQQJ4d",
    "https://www.instagram.com/nsah_hoa?igsh=MWs0Z3F0cWx6NjIyZg=="]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render(sidebar=True, justify_content='center')

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.markdown("<h4 style = 'text-align: center;'>Follow us on social media</h4>", unsafe_allow_html=True)
social_media_icons.render(sidebar=False, justify_content='center')
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






