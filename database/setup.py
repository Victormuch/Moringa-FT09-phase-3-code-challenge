# database/setup.py

import sqlite3

def create_tables():
    conn = sqlite3.connect('magazine.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Magazine (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Author (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Article (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES Author(id),
            FOREIGN KEY (magazine_id) REFERENCES Magazine(id)
        )
    ''')

    conn.commit()
    conn.close()
