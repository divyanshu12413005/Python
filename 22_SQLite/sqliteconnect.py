import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS student (
        st_id INTEGER PRIMARY KEY AUTOINCREMENT,
        st_name TEXT,
        st_class TEXT,
        st_email TEXT
    )
""")

conn.close()
