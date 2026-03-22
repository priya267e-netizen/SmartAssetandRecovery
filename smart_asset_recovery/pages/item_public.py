import streamlit as st
from database import cursor
from notification import send_notification

item_id = st.session_state.get("item_id")

cursor.execute(
    "SELECT name, photo, owner_email FROM items WHERE item_id=?",
    (item_id,)
)
data = cursor.fetchone()

if data:
    name, photo, owner_email = data
    st.title("Item Found")
    st.write(name)
    st.image(photo, width=300)

    # Capture location and send email
    st.write("Your location will be sent to the owner...")
    st.components.v1.html(
        f"""
        <script>
        navigator.geolocation.getCurrentPosition(function(position) {{
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            fetch("/location", {{
                method: "POST",
                headers: {{"Content-Type":"application/json"}},
                body: JSON.stringify({{latitude: lat, longitude: lon, item_id: "{item_id}", owner_email: "{owner_email}"}})
            }});
        }});
        </script>
        """,
        height=0
    )
else:
    st.error("Item not found")