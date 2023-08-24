#!/usr/bin/python3
"""
Script to retrieve and display states with names 
matching a given argument from a MySQL database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve states that match the provided argument.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    try:
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cur.execute(query, (state_name,))
        states = cur.fetchall()
        
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if db:
            db.close()
