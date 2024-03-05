import datetime
import sqlite3

from main import path

# connect to the database
conn = sqlite3.connect(path)
c = conn.cursor()

# select all the rows from the table
c.execute("SELECT * FROM medic")
rows = c.fetchall()

# loop through each medicine and ask the user to confirm taking the dosage
for row in rows:
    medicine_name = row[2]
    dosage = row[4]
    container = row[6]

    # ask the user to confirm taking the dosage
    confirmation = input(
        "Did you take your {} dosage? (y/n) ".format(medicine_name)
    )  # noqa: E501
    if confirmation.lower() == "y":
        # subtract the dosage from the container
        container -= dosage

        # update the last_updated column to today's date
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        c.execute(
            "UPDATE medic SET drug_container=?, last_updated=? WHERE medicine=?",  # noqa: E501
            (container, current_date, medicine_name),
        )

        print("Updated drug container for {}.".format(medicine_name))
    else:
        print("Drug container for {} was not updated.".format(medicine_name))

conn.commit()
conn.close()
