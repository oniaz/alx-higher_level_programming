#!/usr/bin/python3
"""listing all states that start with 'N' from the database hbtn_0e_0_usa"""

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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
