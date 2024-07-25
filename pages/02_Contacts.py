import streamlit as st

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

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