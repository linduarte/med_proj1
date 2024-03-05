# medication_tracker.py

import datetime
import sqlite3

import pandas as pd
from tabulate import tabulate


class DrugTracker:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def update_db(self):
        # select all the rows from the table
        self.c.execute("SELECT * FROM medic")
        rows = self.c.fetchall()

        # loop through each medicine and ask the user to confirm taking the dosage # noqa: E501
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
                self.c.execute(
                    "UPDATE medic SET drug_container=?, last_updated=? WHERE medicine=?",  # noqa: E501
                    (container, current_date, medicine_name),
                )

                print("Updated drug container for {}.".format(medicine_name))
            else:
                print(
                    "Drug container for {} was not updated.".format(
                        medicine_name
                    )  # noqa: E501
                )  # noqa: E501

        self.conn.commit()

    def refill_container(self):
        # Get drugs with containers that need to be refilled
        self.c.execute(
            "SELECT medicine, drug_container, stock_medicine_box FROM medic WHERE drug_container=0"  # noqa: E501
        )
        results = self.c.fetchall()

        # Check if any drugs need to be refilled
        if len(results) == 0:
            print("No drugs need to be refilled.")
        else:
            print("The following drugs containers need to be refilled:")
            for row in results:
                medicine = row[2]
                stock_medicine_box = row[3]
                print(medicine + " (" + str(row[2]) + ")")
                refill_qty = int(
                    input(
                        "Refill "
                        + medicine
                        + " container with "
                        + str(stock_medicine_box)
                        + " units. How many units do you want to refill? "
                    )
                )
                new_stock = stock_medicine_box - refill_qty
                new_container = refill_qty
                self.c.execute(
                    "UPDATE medic SET stock_medicine_box=?, drug_container=? WHERE medicine=?",  # noqa: E501
                    (new_stock, new_container, medicine),
                )

        self.conn.commit()

    def access_db(self):
        df = pd.read_sql_query(
            "SELECT * FROM medic",
            self.conn,
        )

        # Verify that result of SQL query is stored in the dataframe
        print(tabulate(df, headers="keys", tablefmt="psql"))  # type: ignore

    def __del__(self):
        self.conn.close()
