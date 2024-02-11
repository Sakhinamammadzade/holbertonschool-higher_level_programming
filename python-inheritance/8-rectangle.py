#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry():
    """Base Geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")

    

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Test case"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

