#!/usr/bin/python3

""" Define a Square class that inherits from Rectange """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a Square """

    def __init__(self, size):
        """ Initialize a square
            Args:
                - size: size of the square
            Args must be validated by integer_validator (BasseGeometry) """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
