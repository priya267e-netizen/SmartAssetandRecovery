import smtplib

def send_notification(owner_email, item_id, lat, lon):
    maps_link = f"https://maps.google.com/?q={lat},{lon}"
    message = f"""Subject: Item Found

Your item has been found!

Item ID: {item_id}

Finder Location: {maps_link}
"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password")
    server.sendmail(
        "your_email@gmail.com",
        owner_email,
        message
    )
    server.quit()