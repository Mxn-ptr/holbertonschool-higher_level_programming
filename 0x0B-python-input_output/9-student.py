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

    def to_json(self):
        """ Returns the dictionary description """
        return self.__dict__
