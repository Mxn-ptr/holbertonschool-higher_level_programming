#!/usr/bin/python3
""" Define une read function """


def read_file(filename=""):
    """ read_file: print the content of the arg
        Arg:
            filename (file): file to print the content """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
