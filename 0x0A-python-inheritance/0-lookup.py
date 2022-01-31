#!/usr/bin/python3

"""Define an function to returns the list of available attribute and methods"""


def lookup(obj):
    """ Function to returns the list of available attribute and methods """
    return dir(obj)
