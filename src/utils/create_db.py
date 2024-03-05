import sqlite3

from main import path

conn = sqlite3.connect(path)


cursor = conn.cursor()

# create a table
cursor.execute(
    """CREATE TABLE medic
                  (idx_column INTEGER,last_updated TEXT,
                  medicine TEXT PRIMARY KEY,
                  stock_medicine_box INTEGER,
                  drug_dosage INTEGER,
                  prescription_valid_until TEXT,drug_container INTEGER)
               """
)
