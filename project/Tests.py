import os
import sqlite3


# test functions
def test_store_exists():
    if os.path.exists('../data/Store.sqlite'):
        print('Store found Successfully')
        return True
    else:
        print('Store not found')
        return False
    
# test table exists or not
def test_table_exists(name):
    conn = sqlite3.connect('../data/Store1.sqlite')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {name};")
    result = cursor.fetchone()

    conn.close()

    if result:
        print(f"Table {name} exists.")
    else:
        print(f"Table {name} does not exist.")
    
# run tests
def run_tests():
    if test_store_exists():
        test_table_exists('PRIMAP')
        test_table_exists('Diseases')
        
run_tests()