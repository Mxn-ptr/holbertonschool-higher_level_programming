#!/usr/bin/python3

""" Define a function """


def inherits_from(obj, a_class):
    """ inherits_from:
        Args:
            - obj: object we want to compare
            - a_class: class we want to compare with object
        Return: True if object is an instance of the class
                that inherited (directly or indirectly) from a specified class
                False otherwise """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
