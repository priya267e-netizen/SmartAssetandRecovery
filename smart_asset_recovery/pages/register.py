import streamlit as st
from auth import register_user

st.title("Register")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    try:
        register_user(email, password)
        st.success("Account created! You can now log in.")
    except Exception as e:
        st.error("Error: Email may already be registered.")