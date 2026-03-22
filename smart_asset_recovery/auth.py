import bcrypt
from database import cursor, conn

def register_user(email, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO users(email, password, role) VALUES (?, ?, ?)",
                   (email, hashed, "user"))
    conn.commit()

def login_user(email, password):
    cursor.execute("SELECT password, role FROM users WHERE email=?", (email,))
    result = cursor.fetchone()
    if result:
        stored_password, role = result
        if bcrypt.checkpw(password.encode(), stored_password):
            return role  # Return role for later use
    return None