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
    username = argv[1]
    password = argv[2]
    database = argv[3]
    search_name = argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(query, (search_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
