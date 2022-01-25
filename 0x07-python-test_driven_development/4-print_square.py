#!/usr/bin/python3

"""
Define a print square function
"""


def print_square(size):
    """ Function: print_square
        Args: 
            size (int): size of the square
        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        No return just print the square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
