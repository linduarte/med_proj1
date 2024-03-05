# Create add_data.py
import sqlite3

from main import path

conn = sqlite3.connect(path)
cursor = conn.cursor()

medic = [
    (1, "07/05/2023", "Losartana", 30, 2, "30/05/2023", 2),
    (2, "07/05/2023", "AAS", 30, 1, "30/05/2023", 1),
    (3, "07/05/2023", "Anlodipino", 30, 1, "30/05/2023", 1),
    (4, "07/05/2023", "Hidroclorotiazida", 30, 1, "30/05/2023", 1),
    (5, "07/05/2023", "Atorvastatina", 30, 1, "30/05/2023", 1),
]

cursor.executemany("INSERT INTO medic VALUES (?,?,?,?,?,?,?)", medic)
conn.commit()
