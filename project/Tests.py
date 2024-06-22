import os
import sqlite3
import sys

# test functions


def test_store_exists():
    entries = os.listdir('/data')

    # Filter out files from directories
    files = [entry for entry in entries if os.path.isfile(entry)]

    # Print the list of files
    print("Files in the current directory:")
    for file in files:
        print(file)
    if os.path.exists('./data/Store.sqlite'):
        print('Store found Successfully')
        return True
    else:
        print(os.getcwd())
        print('Store not found')
        sys.exit(1)

# test table exists or not


def test_table_exists(name):
    conn = sqlite3.connect('../data/Store.sqlite')
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {name};")
        result = cursor.fetchone()
    except sqlite3.OperationalError as e:
        print(f"Error: {e}. Table {name} does not exist.")
        conn.close()
        sys.exit(1)

    conn.close()

    if result:
        print(f"Table {name} exists.")
    else:
        print(f"Table {name} does not exist.")
        sys.exit(1)

# run tests


def run_tests():
    if test_store_exists():
        test_table_exists('PRIMAP')
        test_table_exists('Diseases')
    else:
        sys.exit(1)


run_tests()
