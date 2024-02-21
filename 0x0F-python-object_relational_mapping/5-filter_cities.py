#!/usr/bin/python3
"""listing all cities for a given state"""
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

    cur.execute("SELECT cities.name FROM cities " +
                "JOIN states ON cities.state_id = states.id " +
                "WHERE states.name = BINARY %s " +
                "ORDER BY cities.id", (argv[4], ))

    rows = cur.fetchall()
    print(f", ".join(f"{row[0]}" for row in rows))

    cur.close()
    db.close()
