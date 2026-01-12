import sqlite3

def create_database():
    conn = sqlite3.connect('users_face.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS People (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        sex TEXT
    )''')
    conn.commit()
    conn.close()

def insert_user(name, age, sex):
    conn = sqlite3.connect('users_face.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO People (name, age, sex) VALUES (?, ?, ?)", (name, age, sex))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

