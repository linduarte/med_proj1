import sqlite3

from main import path

conn = sqlite3.connect(path)

cursor = conn.cursor()

sql = "DELETE FROM medic"

cursor.execute(sql)
conn.commit()
