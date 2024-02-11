#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function"""
    with open(filename) as f:
        return json.loads(f.read())
