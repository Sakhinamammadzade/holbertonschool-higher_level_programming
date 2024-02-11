#!/usr/bin/python3
"""Save Object to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
