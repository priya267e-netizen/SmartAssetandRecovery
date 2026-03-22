import sqlite3
import os

# Create directories if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("uploads", exist_ok=True)
os.makedirs("qrcodes", exist_ok=True)

conn = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items(
        item_id TEXT PRIMARY KEY,
        owner_email TEXT,
        name TEXT,
        description TEXT,
        photo TEXT,
        location TEXT,
        status TEXT
    )
    """)
    conn.commit()