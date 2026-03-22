import streamlit as st
import uuid
import os
from database import cursor, conn
from qr_generator import generate_qr

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

os.makedirs("uploads", exist_ok=True)

st.title("Register Item")

name = st.text_input("Item Name")
description = st.text_area("Description")
location = st.text_input("Location")
photo = st.file_uploader("Upload Photo")

if photo:
    st.image(photo, width=300)
    if st.button("Save Item"):
        item_id = str(uuid.uuid4())[:8]
        path = f"uploads/{item_id}.png"
        with open(path, "wb") as f:
            f.write(photo.read())
        cursor.execute(
            "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?)",
            (item_id, st.session_state.user, name, description, path, location, "active")
        )
        conn.commit()
        qr_path = generate_qr(item_id)
        st.success("QR Generated!")
        st.image(qr_path)