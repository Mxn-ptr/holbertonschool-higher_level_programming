#!/usr/bin/python3

""" Define a rebel class MyInt inherits from int """


class MyInt(int):
    """ Represent a rebel class of int """

    def __eq__(self, other):
        """ Invert operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert operator """
        return super().__eq__(other)
