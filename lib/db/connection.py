import sqlite3
import os

DB_PATH ="wifi_payment.db"
INIT_SCRIPT = os.path.join(os.path.dirname(__file__), "init.sql")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
   with get_connection() as conn, open(INIT_SCRIPT) as f:
       conn.executescript(f.read())