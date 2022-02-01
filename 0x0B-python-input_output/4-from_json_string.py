#!/usr/bin/python3

""" Define a function from json string """
import json


def from_json_string(my_str):
    """ Returns an object represented b a JSON string """
    return json.loads(my_str)
