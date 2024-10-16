#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
