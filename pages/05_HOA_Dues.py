import streamlit as st

# Setting the title of the Streamlit app
st.set_page_config(layout="wide", page_title="North San Antonio Hills HOA")

# Setting the title of the Streamlit app
st.markdown("<h1 style='text-align: center;'>North San Antonio Hills HOA</h1>", unsafe_allow_html=True)
st.image("assets/HOA.png", use_column_width=True)

st.header("North San Antonio Hills HOA Dues")

st.write("""
## Pay Your HOA Dues
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

If you know that you have not paid your HOA dues, you can do so by the following means: 
- [Credit Card Payments via Paypal](https://www.paypal.com/donate/?hosted_button_id=LERPRZ6EAMKG6&source=qr) (Paypal account is not required)
- Use the following QR Code from your phone:
""")
st.image("assets/QR Code.png", use_column_width=False)

st.write("""
- Cash payments can be made to the treasurer at the next HOA meeting.
- Check payments can be mailed to the following address:

**PLEASE MAIL YOUR CHECKS TO:**
NSAH-HOA  
4015 Summer Breeze  
SAN ANTONIO, TEXAS 78253 
         
         
PLEASE ALWAYS ENSURE YOU KEEP YOUR RECEIPT FOR YOUR RECORDS.""")


st.write("""We are currently working on setting up a system that will allow you to check your HOA payment effective date to avoid any double payments.""")

