import streamlit as st

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

st.title("Dashboard")

menu = st.sidebar.selectbox(
    "Options",
    ["Add Item", "My Items", "Admin Panel" if st.session_state.role == "admin" else None, "Logout"]
)

if menu == "Add Item":
    import pages.add_item
elif menu == "My Items":
    import pages.my_items
elif menu == "Admin Panel" and st.session_state.role == "admin":
    import pages.admin_panel
elif menu == "Logout":
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()