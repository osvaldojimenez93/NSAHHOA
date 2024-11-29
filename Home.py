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
st.image("assets/HOA.png", use_column_width=True)

# Home page
st.header("Welcome to North San Antonio Hills")


st.write("""
The North San Antonio Hills Homeowners Association (NSAH HOA) is dedicated to maintaining and improving the quality of life in our community. Our website is designed to provide important information about our neighborhood, including upcoming events, news, and resources for residents.
""")

st.write("""
## Latest News
""")

st.write("""
🎅🏼 Santa is coming to North San Antonio Hills on December 12th!

🌲 Santa will arrive at North San Antonio Hills City Park at 6:30 PM, followed by the fire truck at 6:45 PM to begin the neighborhood route. 

🚒 Track Santa and his Elf on the fire truck by scanning the GroupMe link. 

📮 We’re also excited to announce our “Letter to Santa” drop-off location! You can drop off your letters starting December 1st.""")
col1, col2 = st.columns(2)

with col1:
    st.image("assets/Sana_Firetruck.png", use_column_width=True)
with col2:
    st.image("assets/Santa_Letters.png", use_column_width=True )



st.write("""
## Community Information Collection Forms
- [Feedback collection form](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAMAABxo201URFowOVc0NzZTVUVGSThDTTRPSzhJRVhXTC4u) - Give the board feedback/ideas for improvement.
- [Contact collection form](https://forms.office.com/r/kG3HjSEWW1) - Help us keep in touch with you by providing your contact information. This will allow us to send you important updates and information about our community.
""")

st.write("""
## Helpful Community Resources
- [District 6 City Council](https://www.sa.gov/Directory/Departments/Mayor-Council/City-Council/D6)
- [SAWS Website](https://www.saws.org/)
- [CPS Energy Website](https://cpsenergy.com/)
- [Garbage Collection Map](https://gis.sanantonio.gov/swmd/mycollectionday/default.html)
- [Bexar County Propery Maps](https://bexar.trueautomation.com/mapSearch/?cid=110)
- [City of San Antonio Website](https://www.sanantonio.gov/)
""")





