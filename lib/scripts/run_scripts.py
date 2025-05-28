from lib.db.connection import  get_connection
from lib.models.user import User
from lib.models.payment import Payment
from lib.models.wifi_session import WifiSession
import sqlite3

def create_user(username, password):
    conn =get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        user_id = cursor.lastrowid
        print(f"User '{username}' created with ID {user_id}.")
        return User(user_id, username, password)
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
        return get_user_by_username(username)
    finally:
        conn.close()


def get_user_by_username(username):
    conn =get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None

def make_payment(user_id, amount):
    conn =get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (user_id, amount) VALUES (?, ?)", (user_id, amount))
    conn.commit()
    payment_id =cursor.lastrowid
    conn.close()
    print(f"Payment of ksh{amount:.2f} recorded for user ID {user_id}.")
    return Payment(payment_id, user_id, amount)

def start_wifi_session(user_id, duration):
    conn =get_connection()
    cursor = conn.cursor()
    status = 'active'
    cursor.execute( "INSERT INTO wifi_sessions (user_id, duration_minutes, status) VALUES (?, ?, ?)",
        (user_id, duration, status)
    )
    conn.commit()
    session_id =cursor.lastrowid
    conn.close()
    print(f"WiFi session started for user ID {user_id} for {duration} minutes.")
    return WifiSession(session_id, user_id, duration, status)

def get_active_session_for_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, user_id, duration_minutes, status FROM wifi_sessions WHERE user_id = ? AND status = 'active'", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [WifiSession(*row) for row in rows]
