#!/usr/bin/python3

"""
This module defines a script that takes database connections
credentials and search arguments.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    USER = sys.argv[1]
    PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    SEARCH_ARG = sys.argv[4]

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=USER,
                              passwd=PASS, db=MY_DB, charset="utf8")
    cur = db_conn.cursor()

    my_querry = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(my_querry, (SEARCH_ARG,))

    states = cur.fetchall()
    for state in states:
        print(state)

    db_conn.close()
