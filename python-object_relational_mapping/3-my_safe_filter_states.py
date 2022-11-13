#!/usr/bin/python3
"""  takes in arguments and displays all values in states table """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3])

    cur = connector.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s", (argv[4]))

    for row in cur.fetchall():
        print(row)
