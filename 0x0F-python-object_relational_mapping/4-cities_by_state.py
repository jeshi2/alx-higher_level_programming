#!/usr/bin/python3
"""
script that lists all cities from db hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    connect db and retrive cities along with their states
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cursor.execute(query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        if db:
            db.close()
