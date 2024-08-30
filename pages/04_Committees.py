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

st.header("North San Antonio Hills HOA Committees")
st.write("""
   In order to better serve the community and address the needs of our residents as a team, 
         the North San Antonio Hills HOA has established several committees led by board members or members at large.
         If you are interested in joining a committee, please contact the committee chairperson directly.
      
   If you have an idea for a new committee, please contact the HOA board [Here](mailto:president@nsah-hoa.org;vicepresident@nsah-hoa.org;secretary@nsah-hoa.org;assistantsecretary@nsah-hoa.org).""")

# Committees data
committees = {
   "City Community Relations": [
      "Jessica Grigsby",
      "Davin Dukes",
      "Cole Hudson",
      "Osvaldo 'Jim' Jimenez"
   ],
   "Neighborhood Community Relations": [
      "Davin Dukes",
      "Osvaldo 'Jim' Jimenez",
      "Kevin Mantovani",
      "Alan Tuma"
   ],
   "Budget and Finance": [
      "Jessica Grigsby",
      "Mike Dammann",
      "Cole Hudson"
   ],
   "Website and Social Media": [
      "Osvaldo Jimenez",
      "Greg Jones"
   ],
   "Development and Real Estate": [
      "Jessica Grigsby",
      "Cole Hudson",
      "Richard Ramos",
      "Linda Pilar"
   ],
   "Social Events Coordinator": [
      "Looking for volunteers!"
   ],
   "Park Maintenance and Clean Up": [
      "Looking for volunteers!"
   ],
   "Sign Maintenance": [
      "Looking for volunteers!"
   ],
   "Architectural": [
      "Miguel Sanchez",
      "Thomas",
      "Jessica Grigsby"
   ]
}

# Create a table of contents with hyperlinks
st.markdown("## Table of Contents")
for committee in committees.keys():
   st.markdown(f"- [{committee}](#{committee.replace(' ', '-').lower().replace('--', '-')})")

# Create sections for each committee
for committee, members in committees.items():
   st.markdown(f"### {committee}")
   for member in members:
      st.markdown(f"- {member}")