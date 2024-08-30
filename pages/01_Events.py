import streamlit as st
import streamlit.components.v1 as components
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
st.image("assets/HOA.png", use_column_width=True)

st.header("Upcoming Events")
st.write("""
Join us for our upcoming events! We have a variety of activities planned for residents to enjoy and participate in. Mark your calendars and join the fun!

If you would like an event to be added to this calendar, please email us [Here](mailto:assistantsecretary@nsah-hoa.org).""")

components.html(f"""
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FChicago&bgcolor=%23ffffff&title=North%20San%20Antonio%20Hills&showCalendars=0&showTabs=0&src=OTU0NDI4ZjhhNjFiOTkxOWQwOWM5YzdhOTFmYmU4OTZjNjU5NzYxYjc3ZjhmNzJhYjhkNWMxNWJkZThhZjJhOEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23A79B8E&color=%230B8043" style="border:solid 1px #777" width="100%" height="600" frameborder="0" scrolling="no"></iframe>""",
                height=600)