#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """init module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json function"""
        if attrs is None:
            return vars(self)
        else:
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

    def reload_from_json(self, json):
        """Student to disk and reload"""
        for key, value in json.items():
            setattr(self, key, value)
