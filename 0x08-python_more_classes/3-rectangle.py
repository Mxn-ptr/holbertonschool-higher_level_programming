#!/usr/bin/python3

""" Define a Rectangle class """


class Rectangle:
    """ Represent a Rectangle """
    def __init__(self, width=0, height=0):
        """ Init function:
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Function for change the witdh of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Function for change the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ Returns the printable representation of rectangle
        with the character '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i != self.__height - 1:
                rect += "\n"
        return rect
