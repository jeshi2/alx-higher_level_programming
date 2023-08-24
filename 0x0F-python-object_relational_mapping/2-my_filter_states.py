#!/usr/bin/python3
"""
Script to retrieve and display states with names 
matching a given argument from a MySQL database.
"""

import MySQLdb
import sys

def main():
    """
    connect to the database and retrieve filtered states.
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

        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
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

if __name__ == "__main__":
    main()
