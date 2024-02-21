#!/usr/bin/python3
"""listing all states that match the passed argument.
 while safeguarding against SQL injections """

import MySQLdb

if __name__ == "__main__":
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,  # Specify the port here
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = BINARY %s ORDER BY id",
            (argv[4], )
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
