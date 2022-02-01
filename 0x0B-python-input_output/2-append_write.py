#!/usr/bin/python3

""" Define a function to append text in a file """


def append_write(filename="", text=""):
    with open(filename, "a") as file:
        return file.write(text)
