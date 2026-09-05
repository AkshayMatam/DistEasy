import sqlite3

DATABASE = "disteasy.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully!")


create_database()