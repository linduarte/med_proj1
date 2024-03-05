import sqlite3

from main import path

# Connect to database
conn = sqlite3.connect(path)
c = conn.cursor()
# Get drugs with containers that need to be refilled
c.execute(
    "SELECT medicine, drug_container, stock_medicine_box FROM medic WHERE drug_container=0"  # noqa: E501
)
results = c.fetchall()

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
        c.execute(
            "UPDATE medic SET stock_medicine_box=?, drug_container=? WHERE medicine=?",  # noqa: E501
            (new_stock, new_container, medicine),
        )

# Commit changes and close connection
conn.commit()
conn.close()
