# Accessing data stored in SQLite using Python and Pandas

import sqlite3

import pandas as pd
from main import path
from tabulate import tabulate

# Read sqlite query results into a pandas DataFrame

conn = sqlite3.connect(path)


df = pd.read_sql_query(
    "SELECT * FROM medic",
    conn,
)


# Verify that result of SQL query is stored in the dataframe
print(tabulate(df, headers="keys", tablefmt="psql"))  # type: ignore

conn.close()
