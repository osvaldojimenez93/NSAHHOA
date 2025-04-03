import streamlit as st
from st_social_media_links import SocialMediaIcons

def render_page_template(title: str):
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
        st.image("assets/HOA.png", use_container_width=True)

        st.header(f"{title}")
