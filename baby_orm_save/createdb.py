import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Users")
c.execute("""CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    username VARCHAR,
    email VARCHAR,
    created_at DATE,
    updated_at DATE
)""")
conn.commit()
conn.close()