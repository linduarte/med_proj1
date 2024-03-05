# main.py
from medication_tracker import DrugTracker

path = r"C:\Users\clldu\OneDrive\vsc_envir\first_project\project\database\my_drugs.db"  # noqa: E501
tracker = DrugTracker(path)
tracker.update_db()
tracker.refill_container()
tracker.access_db()

if __name__ == "__main__":
    print("main.py")
