#!/usr/bin/python3

""" Define a class Student """
import json


class Student:
    """ Represents a Student """
    def __init__(self, first_name, last_name, age):
        """ Initialize a student
        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary description
            Arg:
                - attrs : list of attributes """
        my_dict = dict()
        if type(attrs) is list and all(type(el) is str for el in attrs):
            for el in attrs:
                if el in self.__dict__:
                    my_dict.update({el: self.__dict__[el]})
            return my_dict
        return self.__dict__
