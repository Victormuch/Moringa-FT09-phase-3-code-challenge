import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    conn = sqlite3.connect("magazine.sqlite")
    conn.row_factory = sqlite3.Row
    return conn
