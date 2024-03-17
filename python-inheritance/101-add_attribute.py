#!/usr/bin/python3


def add_attribute(obj, attribute, value):
    """Add attribute to the object if possible, otherwise raise TypeError."""
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
