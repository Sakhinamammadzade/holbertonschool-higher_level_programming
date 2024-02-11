#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """Function for write a file"""
    with open(filename, "w") as f:
        return f.write(text)
