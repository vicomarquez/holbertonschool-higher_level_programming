#!/usr/bin/python3
""" lists all states with a name starting with N """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                database=argv[3])

    cur = connector.cursor()

    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%' OR NAME LIKE 'n%'")

    for row in cur.fetchall():
        print(row)
