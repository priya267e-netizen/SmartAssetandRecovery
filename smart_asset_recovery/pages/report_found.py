import streamlit as st
from database import cursor,conn

# protection
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Login required")
    st.stop()

st.title("Report Found Item")

item = st.text_input("Item ID")

message = st.text_area("Message")

location = st.text_input("Location")

if st.button("Submit"):

    cursor.execute(
    "INSERT INTO reports(item_id,finder_location,message) VALUES (?,?,?)",
    (item,location,message)
    )

    conn.commit()

    st.success("Report submitted")