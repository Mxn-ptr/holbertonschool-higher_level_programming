#!/usr/bin/python3

""" Define a function to append text in a file """


def append_write(filename="", text=""):
    """ append_write: append text in a file """
    with open(filename, "a") as file:
        return file.write(text)
