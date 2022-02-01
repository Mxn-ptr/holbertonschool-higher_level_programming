#!/usr/bin/python3

""" Define a function to write into a file """


def write_file(filename="", text=""):
    """ write_file : write a text into a file
        Args:
            filename (file): name of the file to write into
            text (str): text to add in the file """
    with open(filename, "w") as file:
        return file.write(text)
