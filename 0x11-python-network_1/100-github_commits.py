#!/usr/bin/python3
"""Python script that takes 2 arguments"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(sys.argv[1], sys.argv[2]))
    if r.status_code >= 400:
        print("None")
    else:
        for commit in r.json()[:10]:
            print("{}: {}".format(commit.get("sha"),
                                  commit.get("commit")
                                  .get("author").get("name")))
