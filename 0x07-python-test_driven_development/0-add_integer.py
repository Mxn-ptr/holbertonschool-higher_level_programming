#!/usr/bin/python3

""" Defines an integers addition function """


def add_integer(a, b=98):
    """ Function : add_integers
    Args:
            a : int or float
            b : int or float
    Raise:
            TypeError: if a or b are not int or float
    Returns : sum of a and b """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
