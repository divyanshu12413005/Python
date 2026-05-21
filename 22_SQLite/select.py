import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM STUDENT")

for n in data:
    print(n[0],n[1],n[2],n[3])