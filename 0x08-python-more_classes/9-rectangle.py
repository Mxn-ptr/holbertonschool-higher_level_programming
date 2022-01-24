#!/usr/bin/python3

""" Define a Rectangle class """


class Rectangle:
    """ Represent a Rectangle
        Attributes:
            number_of_instances: number of rectangle instances
            print_symbol: symbol to print the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Init function:
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        type(self).number_of_instances += 1
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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Function: bigger_or_equal
            Args:
                rect_1: first rectangle to compare
                rect_2: second rectangle to compare
            Return: the bigger rectangle or rect_1 if equal """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size """
        return (cls(size, size))

    def __str__(self):
        """ Returns the printable representation of rectangle
        with the character '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete a rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
