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

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        data = []
        filename = f"{cls.__name__}.json"
        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Json string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance"""
        if cls.__name__ == 'Square':
            dummy = cls(5)
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        dummy.update(**dictionary)
        return dummy
