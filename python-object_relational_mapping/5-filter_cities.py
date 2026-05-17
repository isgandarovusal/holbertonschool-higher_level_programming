#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
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

    # JOIN istifadə edərək ştat adına görə şəhərləri seçirik
    # SQL injection-dan qorunmaq üçün %s parametrləşdirilmiş sorğudan istifadə
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))

    # Nəticələri bir siyahıya (list) yığırıq
    query_rows = cur.fetchall()
    cities = [row[0] for row in query_rows]

    # Şəhərləri vergüllə birləşdirib çap edirik
    print(", ".join(cities))

    # Bağlantıları kəsirik
    cur.close()
    db.close()
