#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost",
            port=3306, 
            user=argv[1],
            passwd=argv[2],
            database=argv[3])

    cur = connector.cursor()

    cur.execute("SELECT * FROM states")

    for row in cur.fetchall():
        print(row)
