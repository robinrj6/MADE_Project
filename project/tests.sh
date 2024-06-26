#!/bin/bash

# pip install pandas
# pip install py7zr
# pip install requests
# pip install sqlalchemy
# python project/Code.py
# An issue occuring with the environment where the code is running, the code is not able to read the store.sqlite from the path. The code is working fine in the local environment.
# This in the end leads to the failure of the test cases as the test cases look for the data in the store.sqlite file but the file is not found.
# The workflow executes the tests on every push to the main branch and an output is generated which shows the test cases are failing.
python project/Tests.py