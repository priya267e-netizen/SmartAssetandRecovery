import streamlit as st
from database import create_tables

# create database tables
create_tables()

# default session values
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

# check QR scan
query = st.query_params

if "item" in query:

    st.session_state.item_id = query["item"]

    import pages.item_public

else:

    if not st.session_state.logged_in:

        import pages.login

    else:

        import pages.dashboard