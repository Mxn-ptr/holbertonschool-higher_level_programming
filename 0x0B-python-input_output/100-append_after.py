#!/usr/bin/python3

""" Define a function """


def append_after(filename="", search_string="", new_string=""):
    """ append_after: append a new_string after a specified string
        Args:
            filename (file): file to search and add text
            search_string (str): specified string to search
            new_string (str): new string to add after search_string """
    text = ""
    with open(filename, "r") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as file:
        file.write(text)
