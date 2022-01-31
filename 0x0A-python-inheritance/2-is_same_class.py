#!/usr/bin/python3

""" Define a function """


def is_same_class(obj, a_class):
    """ is_same_class:
        Args:
            - obj: object we want to compare
            - a_class: class we want to compare with object
        Return: True if object is exactly an instance of the class,
                False otherwise """
    if type(obj) == a_class:
        return True
    return False
