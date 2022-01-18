#!/usr/bin/python3
from ctypes import sizeof


class Square:
    '''
    Define a classe Square
    Private instance attribute : size (int)
        - property def size(self)
        - property setter def size(self, value)
    '''
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
    '''
    Public instance method : returns the current square area
    '''
    def area(self):
        return (self.__size * self.__size)

    '''
    Public instance method : print the square
    '''
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
