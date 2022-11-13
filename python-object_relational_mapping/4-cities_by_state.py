#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3])

    cur = connector.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = state_id "
                "ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)
