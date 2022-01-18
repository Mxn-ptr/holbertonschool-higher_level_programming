#!/usr/bin/python3


" Define a class Square Empty "


class Square:
    """
    Define a classe Square

    Attribute:
        size (int): size of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """area returns the current square area"""
    def area(self):
        return (self.__size * self.__size)
