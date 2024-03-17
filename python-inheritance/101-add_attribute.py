#!/usr/bin/python3
"""add_attribute"""


def add_attribute(obj, attribute, value):
    """Add attribute to the object if possible, otherwise raise TypeError."""
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    if not isinstance(attribute, str):
        raise TypeError("attribute name must be a string")
    if hasattr(obj, attribute):
        raise TypeError("attribute already exists")
    
    setattr(obj, attribute, value)
