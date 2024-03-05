import sqlite3

import pandas as pd
from main import path

conn = sqlite3.connect(path)
cur = conn.cursor()
info = cur.execute("PRAGMA table_info('medic')").fetchall()
columns = [item[0] for item in cur.description]

df = pd.DataFrame(info, columns=columns)


print(df)
