#!/usr/bin/python3

"""
This module will implement a script to fetch and print
all state from a database
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db_conn = MySQLdb.connect(host="localhost", port=3306,
                              user=USER, passwd=PASS, db=DB)
    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    db_conn.close()
