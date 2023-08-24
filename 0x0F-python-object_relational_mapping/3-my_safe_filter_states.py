#!/usr/bin/python3
"""
script that display all values in states table of hbtn_0e_0_usa
where name matches the provided arg(safe from SQL Injection
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    connect db and retrive states that matches 
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if db:
            db.close()
