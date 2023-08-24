#!/usr/bin/python3
"""
Script to retrieve and display states with names 
matching a given argument from a MySQL database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access the database and retrieve the states
    that match the criteria
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
