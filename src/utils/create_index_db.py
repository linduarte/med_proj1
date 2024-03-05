import sqlite3

from main import path

conn = sqlite3.connect(path)

cursor = conn.cursor()

cursor.execute(
    """
    CREATE INDEX idx_med ON medic (idx_column);
"""
)
