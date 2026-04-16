import bcrypt
import sqlite3
from database import DB_NAME


def register_user(username, password, role):
    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8") 

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, hashed, role))


def login_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT password, role FROM users
            WHERE username = ?
        """, (username,))
        user = cursor.fetchone()

        if not user:
            return None

        stored_password, role = user

        stored_password_bytes = stored_password.encode("utf-8") if isinstance(stored_password, str) else stored_password

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password_bytes
        ):
            return role

        return None