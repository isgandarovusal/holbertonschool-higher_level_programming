#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument,
safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

    # Sətiri bölərək pycodestyle limitini qoruyuruq
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Nəticələri çap edirik
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Bağlantıları kəsirik
    cur.close()
    db.close()
