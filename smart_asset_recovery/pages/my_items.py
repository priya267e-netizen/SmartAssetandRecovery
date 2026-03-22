import streamlit as st
import pandas as pd
from database import conn

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

st.title("My Items")

email = st.session_state.user
query = "SELECT * FROM items WHERE owner_email=?"

df = pd.read_sql(query, conn, params=(email,))
st.dataframe(df)