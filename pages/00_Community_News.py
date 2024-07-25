import streamlit as st
# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

st.header("Community News")
st.write("""
    Stay updated with the latest news and announcements from the North San Antonio Hills HOA. Check back regularly for updates on community events, projects, and other important information.
    """)
st.write("""
# North San Antonio Hills Homeowners Association

## June 2024 Quarterly Update

### Greeting from the President & HOA Board

#### Hello Neighbors,

Thank you to everyone who attended the recent meeting and for your vote of trust and confidence. As your newly elected President, I am excited to serve our community alongside the new HOA board. We will work diligently to inform and represent all members of the HOA equally and fairly, ensuring that everyone's opinion is heard and making all decisions impartially.

Our vision is to foster a strong, inclusive community and enhance property values. The strength of our neighborhood lies in the unity and collaboration of its members. The HOA is here to support you and address any concerns. We are committed to maintaining the aesthetics, safety, and facilities of our community to ensure resident satisfaction. Throughout the year, we will organize events and workshops to engage with neighbors. Your participation and feedback are vital in shaping our community's future.

Please feel free to reach out to us with any suggestions, questions, or if you wish to get involved in community initiatives. Together, we can make a significant and positive impact on our beloved neighborhood.

We are excited to serve you as the newly elected board this year.

Best regards,  
**Jessica Grigsby**

### NSAH Board of Directors 2024-2025

| Position                | Name                 | Email                         |
|-------------------------|----------------------|-------------------------------|
| President (E)           | Jessica Grigsby      | Jgrigsby.nsah@outlook.com     |
| Vice President (A)      | Davin Dukes          | Davduke8@gmail.com            |
| Secretary (E)           | Cole Hudson          | m.cole.hudson@gmail.com       |
| Assistant Secretary (A) | Osvaldo 'Jim' Jimenez| Baldo727@gmail.com            |
| Treasurer (E)           | Mike Dammann         | mdammann@satx.rr.com          |
| Architectural Chair (A) | Miguel Sanchez       | msanchez@meta-engr.com        |

**(A) indicates appointed positions, (E) indicates elected positions**

### Community Projects and News

#### Autumn Mist Closure

Over the last couple of weeks, the city has placed signage across all main roads leading to Autumn Mist to inform people of the Autumn Mist Closure in and out of Alamo Ranch. The road has been closed as of June 15th and will remain temporarily closed all summer through September 15th. The HOA and City Council will revisit the consensus for next steps based on the majority of our residents’ requests.
""")
st.image("assets/Autumn Mist Closure.png", use_column_width=True)
st.write("""
#### 1604 Access Road Slowdown Lane

According to city staff, the construction of the deceleration lane is scheduled to begin in the fall. The HOA board will be in close communication with the District 6 office and will provide more details as they become available.

#### Homeless Encampments

Please be aware and remain cautious around the Misty Woods and 1604 greenbelt. It has come to our attention that there is a homeless encampment in the area with approximately 10-20 individuals. The Department of Human Services will be assessing the location and then schedule an abatement (clean-up) of the property.
""")
# Creating a streamlit container with 2 columns
col1, col2 = st.columns(2)

# Displaying the images side by side
with col1:
    st.image("assets/Encampment 1.jpg", use_column_width=True)

with col2:
    st.image("assets/Encampment 2.jpg", use_column_width=True)

st.write("""
#### Commercial Real Estate Notifications

The HOA is still waiting for additional information regarding construction of the initially proposed storage unit. Plans have been designed, and the developer is still waiting for the purchase of the land to finalize. No updates regarding the sale of the property or construction have been provided to the board.

A few of you may have noticed construction equipment in and around Summer Breeze and Enchanted Sunset. Crews have begun clearing pathways to take soil samples for an additional storage complex which means we are expected to have a storage development at both entrances to the neighborhood.
""")
st.image("assets/Construction Equipment.jpg", use_column_width=False)
st.write("""
#### City Councilwoman Point of Contact for NSAH Residents

By now, everyone should have received a postcard from the City Council regarding the June 15th closure. They are interested in hearing your thoughts and collecting additional feedback through the temporary closure.

### HOA Business

#### Architectural Control Committee

All residential and commercial owners planning construction or improvements need to follow the RESTRICTIVE COVENANTS that govern our great community. These covenants can be downloaded from [www.northsahills.com](http://www.northsahills.com) or obtained from any Board member.

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
4128 AUTUMN MIST  
SAN ANTONIO, TEXAS 78253  


### CALLING ALL NEIGHBORS!!!

The HOA is here to help our community thrive but we can't do it alone! Your involvement is crucial in making our neighborhood a better place to live. We need your ideas, feedback, and participation to achieve our goals.

Join us and let your voice be heard!

         """)