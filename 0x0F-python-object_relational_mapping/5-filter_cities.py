#!/usr/bin/python3
"""Module task 4"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd='', db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT `cities`.`name`\
                FROM `cities`\
                LEFT JOIN `states`\
                ON `states`.`id` = `cities`.`state_id`\
                WHERE `states`.`name` =%s\
                ORDER BY `cities`.`id` ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
