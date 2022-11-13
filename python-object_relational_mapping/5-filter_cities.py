#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
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

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN "
                "states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (argv[4], ))

    print(', '.join([row[1] for row in cur.fetchall()]))
