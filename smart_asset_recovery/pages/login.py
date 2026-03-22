import streamlit as st
from auth import login_user

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    role = login_user(email,password)

    if role:

        st.session_state.logged_in = True
        st.session_state.user = email
        st.session_state.role = role

        st.success("Login success")
        st.rerun()

    else:

        st.error("Invalid login")