import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../../test.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS test_cases (
            id INTEGER PRIMARY KEY,
            user_story TEXT NOT NULL,
            generated_cases TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()