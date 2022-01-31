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
