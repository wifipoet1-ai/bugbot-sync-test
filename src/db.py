import os
import sqlite3

def get_user(conn, user_id):
    # BUG 1: SQL injection via string interpolation into the query
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    return cur.fetchone()

def export_user(user_id, dest):
    # BUG 2: command injection via os.system with unsanitized input
    os.system("cp /data/users/" + user_id + " " + dest)
