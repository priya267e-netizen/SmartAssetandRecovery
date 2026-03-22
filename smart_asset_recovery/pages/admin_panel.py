import streamlit as st
import pandas as pd
from database import conn

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

if st.session_state.role != "admin":
    st.error("Access denied. Admins only.")
    st.stop()

st.title("Admin Panel")

users = pd.read_sql("SELECT * FROM users", conn)
items = pd.read_sql("SELECT * FROM items", conn)

st.subheader("Users")
st.dataframe(users)

st.subheader("Items")
st.dataframe(items)

delete_id = st.text_input("Delete Item ID")

if st.button("Delete Item"):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE item_id=?", (delete_id,))
    conn.commit()
    st.success("Item deleted")