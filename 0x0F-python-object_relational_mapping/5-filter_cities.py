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
    the_state = sys.argv[4]

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=USER,
                              passwd=PASS, db=MY_DB, charset="utf8")
    cur = db_conn.cursor()

    my_querry = ("SELECT cities.id, cities.name, states.name "
                 "FROM cities INNER JOIN states "
                 "ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
    cur.execute(my_querry, (the_state,))
    cities = cur.fetchall()

    lst = []
    for city in cities:
        lst.append(city[1])
    output = ', '.join(map(str, lst))
    print(output)

    db_conn.close()
