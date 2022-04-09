#!/usr/bin/python3
"""Module task 0"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd='', db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
