import sqlite3

import pandas as pd
from main import path

# connect to the database
conn = sqlite3.connect(path)

# create a pandas dataframe from the database table
df = pd.read_sql_query("SELECT * from medic", conn)


# print the dtypes of each column in the dataframe
print(df.dtypes)

# close the database connection
conn.close()
