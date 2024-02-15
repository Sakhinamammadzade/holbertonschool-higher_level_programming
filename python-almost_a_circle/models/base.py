#!/usr/bin/python3
"""Base Class"""
import json


class Base():
    """Define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            with open("Rectangle.json", "w") as outfile:
                return json.dumps(list_dictionaries)
