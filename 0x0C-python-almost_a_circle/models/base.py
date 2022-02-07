#!/usr/bin/python3

""" Define a Base class """
import json


class Base:
    """ Represents a base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the base
            Arg:
                id (int): number of the id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return JSON representation of an object(string) """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save the dictionary to a JSON file
            Arg:
                - cls (class): class
                - list_objs: list of the objects to save """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dicts = [dict.to_dictionary() for dict in list_objs]
                jfile.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
