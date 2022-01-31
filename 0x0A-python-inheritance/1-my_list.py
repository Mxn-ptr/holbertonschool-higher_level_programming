#!/usr/bin/python3

""" Define a MyList class that inherits from list """


class MyList(list):
    """ Class MyList """

    def print_sorted(self):
        """ Print a sorted list """
        print(sorted(self))
