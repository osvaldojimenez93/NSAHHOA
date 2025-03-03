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

st.header("Community News")
st.write("""
    Stay updated with the latest news and announcements from the North San Antonio Hills HOA. Check back regularly for updates on community events, projects, and other important information.
    """)
st.link_button("Previous Newsletters", url="https://drive.google.com/drive/folders/1lRPQZ_-CGeTOsJg_zlrDBBlxrothUD96?usp=sharing")


st.write("""
# North San Antonio Hills Homeowners Association

## February 2025 Quarterly Update

### Greeting from the President & HOA Board

#### Hello Neighbors,

As we welcome the new year, your HOA Board is excited to continue working with our community to maintain and improve the wonderful neighborhood we all call home. 

In this newsletter, you’ll find updates on ongoing projects, important news from our established committees, and some upcoming events to look forward to this year.

We encourage everyone to get involved in community activities and share ideas to enhance our neighborhood via our HOA website at nsah-hoa.org. Together, we can make 2025 another great year for our community and residents!


Best regards,  
**Davin Dukes**
HOA Vice President

### NSAH Board of Directors 2024-2025

| Position                | Name                 | Email                         |
|-------------------------|----------------------|-------------------------------|
| President            | Jessica Grigsby      | president@nsah-hoa.org     |
| Vice President       | Davin Dukes          | vicepresident@nsah-hoa.org           |
| Secretary            | Cole Hudson          | secretary@nsah-hoa.org       |
| Assistant Secretary  | Osvaldo 'Jim' Jimenez| assistantsecretary@nsah-hoa.org            |
| Treasurer            | Mike Dammann         | treasurer@nsah-hoa.org          |
| Architectural Chair  | Miguel Sanchez       | architect@nsah-hoa.org        |


### Community Projects and News

#### Upcoming Events

| Date                | Time   | Event Description                                                                 |
|---------------------|--------|-----------------------------------------------------------------------------------|
| Saturday, March 29  | 9am    | Annual NSAH HOA Breakfast in the Park|
| Saturday, April 26  | 10-11:30am | Clean Up day/Volunteer Opportunity|


Keep an eye on www.nsah-HOA.org for more events and neighborhood news!         

#### Area Beautification

Roadrunner Park Maintenance: Community volunteers recently came together to clean and revitalize the park. Old rotting benches were removed, and overgrown areas were cleared, making the space safer and more inviting for all residents. Overall maintenance and upkeep of overgrowth has been provided on a volunteer basis by residents helping cut the grass with their mowing equipment. """)
st.image("assets/Maintenance.png", use_container_width=True)
st.write("""
HOA Sign Maintenance: A very special thanks to our neighbor Jana Mantovani for taking the lead on beautifying our HOA entrance sign. It underwent power washing, cleanup, and existing lighting was fixed to ensure better visibility for those entering our neighborhood.""")
st.image("assets/HOANight.png", use_container_width=True)
st.write("""
#### Join us for a Clean-Up Day! 

**What:** Help make our community a cleaner, greener place by volunteering to pick up litter.  
**When:** SATURDAY, APRIL 26 @ 10:00 AM  
**Where:** Meet at the dentists’ office by Nardis Gun Club to help pick up trash along the frontage road between Valley Meadow and Misty Woods.  
**Contact:** Jana Mantovani @ (210) 779-8030

""")
st.write("""
#### City and TxDOT Communications

Deceleration lane at the valley meadow entrance is set to begin at the end of February. The board will keep in contact with the city on updates/delays/expected completion times. 

If you have not had a chance to venture to the southwest end of the neighborhood, the City park improvements are now complete and include a new play area for kids. 

### Commercial Real Estate Notifications

Update regarding the storage site construction on Misty Woods: Construction is well underway as everyone can see when driving by the misty woods exit. Construction was started ~1 month late in October and is expected to take a full year to complete. The board is aware of the stop sign in that area being rotated as construction equipment flows in and out of the area. We are in contact with the contractor and they have acknowledged they will fix the stop sign. There is a new monument that is expected to be built after construction is complete along with a brick retaining wall built at the rear of the property. 

### HOA Business

#### Architectural Control Committee

All residential and commercial owners planning construction or improvements need to follow the RESTRICTIVE COVENANTS that govern our great community. These covenants can be downloaded from our [Governing Documents at nsah-hoa.org](https://drive.google.com/drive/folders/1pC58CSJmygh5kCpaBAchsc3IZ_Cime5F?usp=sharing) or obtained from any Board member.

#### Have you paid your yearly dues?

Your $50.00 a year helps to ensure your property values are protected.

- Breakfast in the Park
- Halloween Party
- Newsletter
- Roadrunner Park Maintenance
- Entrance Sign Maintenance
- Communicates with City, County, and State for:
  - Land Use and Zoning
  - Streets and Utilities
  - Nearby Area Developments
  - Subdivision Access
  - Emergency Services

**PLEASE MAIL YOUR CHECKS TO:**

NSAH-HOA  
4015 Summer Breeze  
SAN ANTONIO, TEXAS 78253  


### CALLING ALL NEIGHBORS!!!

The HOA is here to help our community thrive but we can't do it alone! Your involvement is crucial in making our neighborhood a better place to live. We need your ideas, feedback, and participation to achieve our goals.

Join us and let your voice be heard!

         """)