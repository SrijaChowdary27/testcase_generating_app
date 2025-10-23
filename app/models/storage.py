import sqlite3
from .database import DB_PATH

def save_test_case(user_story, generated_cases):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO test_cases (user_story, generated_cases) VALUES (?, ?)",
        (user_story, generated_cases)
    )
    conn.commit()
    conn.close()

def get_all_test_cases():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM test_cases ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return data
 