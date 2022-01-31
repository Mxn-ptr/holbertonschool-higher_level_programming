#!/usr/bin/python3

""" Define a function """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class:
        Args:
            - obj: object we want to compare
            - a_class: class we want to compare with object
        Return: True if object is an instance of the class
                or if object is an instance of a class that inherited from,
                False otherwise """
    if isinstance(obj, a_class):
        return True
    return False
