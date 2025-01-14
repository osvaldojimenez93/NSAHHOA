import streamlit as st
from st_social_media_links import SocialMediaIcons

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

st.header("Contact Us")
st.write("""
We are here to help! If you have any questions, concerns, or suggestions, please feel free to reach out to us. You can contact the North San Antonio Hills HOA directly via the contacts below
         OR submit an anonymous request using the form below:

[NSAH Feedback Form](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAMAABxo201URFowOVc0NzZTVUVGSThDTTRPSzhJRVhXTC4u)
         
""")
st.write("""
# HOA Board Members         
| Position                | Name                 | Email                         |
|-------------------------|----------------------|-------------------------------|
| President (E)           | Jessica Grigsby      | president@nsah-hoa.org     |
| Vice President (A)      | Davin Dukes          | vicepresident@nsah-hoa.org           |
| Secretary (E)           | Cole Hudson          | secretary@nsah-hoa.org       |
| Assistant Secretary (A) | Osvaldo 'Jim' Jimenez| assistantsecretary@nsah-hoa.org            |
| Treasurer (E)           | Mike Dammann         | treasurer@nsah-hoa.org          |
| Architectural Chair (A) | Miguel Sanchez       | architect@nsah-hoa.org        |
""")