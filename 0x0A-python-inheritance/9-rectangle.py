#!/usr/bin/python3

""" Define a Rectangle class that inherits form BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initialise Rectangle:
        Args:
            - width: width of the rectangle
            - height: height of the rectangle
        Args must be validated by integer_validator (BaseGeometry) """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ Return print() and str() of a rectangle """
        return ("[{}] {}/{}"
                .format(str(self.__class__.__name__),
                        str(self.__width), str(self.__height)))
