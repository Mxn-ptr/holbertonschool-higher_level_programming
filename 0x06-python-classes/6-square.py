#!/usr/bin/python3
from ctypes import sizeof


class Square:
    '''
    Define a classe Square
    Private instance attribute : size (int)
        - property def size(self)
        - property setter def size(self, value)
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    '''
    Public instance method : returns the current square area
    '''
    def area(self):
        return (self.__size * self.__size)

    '''
    Public instance method : print the square with position
    '''
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
