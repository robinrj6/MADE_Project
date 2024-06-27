import sqlite3
import os

def read_store(table):
    db_path = '../data/Store.sqlite'
    try:
        # Check if the database file exists
        if not os.path.exists(db_path):
            print(os.getcwd())
            print(f"Database file not found at {db_path}")
            return None

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table};")
        results = cursor.fetchall()
        return results
    except sqlite3.OperationalError as e:
        print(f"Error opening database: {e}")
        return None
    finally:
        if 'conn' in locals():
            conn.close()

primap = read_store('PRIMAP')
diseases = read_store('Diseases')
print(primap)
print(diseases)