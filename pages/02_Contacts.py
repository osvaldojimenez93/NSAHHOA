import streamlit as st
from components.PageTemplate import render_page_template

render_page_template("Contact Us")
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