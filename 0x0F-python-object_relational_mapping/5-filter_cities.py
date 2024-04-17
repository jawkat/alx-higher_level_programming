#!/usr/bin/python3
"""Lists states"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    QUERY = """
      SELECT cities.id, cities.name, states.name FROM cities
      JOIN states ON cities.state_id = states.id
      WHERE states.name = %s
      ORDER BY cities.id ASC;
"""
    cur.execute(QUERY,(argv[4],))
    query_rows = cur.fetchall()
    city_names = [row[1] for row in query_rows]
    print(", ".join(str(city) for city in city_names))
    cur.close()
    conn.close()
