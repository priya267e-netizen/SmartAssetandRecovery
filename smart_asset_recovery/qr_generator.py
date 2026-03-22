import qrcode

def generate_qr(item_id):
    url = f"https://your-app.streamlit.app/?item={item_id}"
    img = qrcode.make(url)
    path = f"qrcodes/{item_id}.png"
    img.save(path)
    return path