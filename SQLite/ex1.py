import sqlite3 as sq  # модуль SQLite3

with sq.connect("saper.db") as con:
    cur = con.cursor()

    con.execute("DROP TABLE IF EXISTS users")
    con.execute(
        """CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )"""
    )
