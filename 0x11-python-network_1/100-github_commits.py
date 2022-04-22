#!/usr/bin/python3
"""Python script that takes 2 arguments"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(sys.argv[1], sys.argv[2]))
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                                  commits[i].get("commit")
                                  .get("author").get("name")))
    except IndexError:
        pass
