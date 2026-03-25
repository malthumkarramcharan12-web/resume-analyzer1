import sqlite3

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY, user_id INTEGER, score REAL)")

    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def save_result(user_id, score):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("INSERT INTO results (user_id, score) VALUES (?, ?)", (user_id, score))
    conn.commit()
    conn.close()

def get_results(user_id):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT score FROM results WHERE user_id=?", (user_id,))
    data = c.fetchall()
    conn.close()
    return data
