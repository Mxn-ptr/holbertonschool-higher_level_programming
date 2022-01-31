#!/usr/bin/python3

""" Define a BaseGeometry class"""


class BaseGeometry:
    """ Represent a base geometry """

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator:
            Args:
                - name (str): name of the variable
                - value (int): value of name
            Raises:
                - TypeError: if value is not an int
                - ValueError: if value <= 0 """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
