import streamlit as st

st.title("🎈 Project Kelompok 11")
import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2006, 12, 22))
st.write("Your birthday is:", d)
