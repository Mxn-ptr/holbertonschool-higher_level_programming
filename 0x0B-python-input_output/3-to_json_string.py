#!/usr/bin/python3

""" Define a function to return the json representation of an object """
import json


def to_json_string(my_obj):
    """ Return JSON representation of an object(string) """
    return json.dumps(my_obj)
