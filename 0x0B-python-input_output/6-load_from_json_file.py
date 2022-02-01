#!/usr/bin/python3

""" Define a function that creates an Object from a "JSON file" """
import json


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)
