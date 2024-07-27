import streamlit as st
import streamlit.components.v1 as components

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

st.header("Upcoming Events")
st.write("""
Join us for our upcoming events! We have a variety of activities planned for residents to enjoy and participate in. Mark your calendars and join the fun!

If you would like an event to be added to this calendar, please email us [Here](mailto:assistantsecretary@nsah-hoa.org).""")

components.html(f"""
<iframe src="https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=America%2FChicago&bgcolor=%23ffffff&title=North%20San%20Antonio%20Hills&showCalendars=0&showTabs=0&src=OTU0NDI4ZjhhNjFiOTkxOWQwOWM5YzdhOTFmYmU4OTZjNjU5NzYxYjc3ZjhmNzJhYjhkNWMxNWJkZThhZjJhOEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&src=ZW4udXNhI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&color=%23A79B8E&color=%230B8043" style="border:solid 1px #777" width="100%" height="600" frameborder="0" scrolling="no"></iframe>""",
                height=600)