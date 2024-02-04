#!/usr/bin/python3
"""Access and update private attribute."""


class Square:
    def __init__(self, size=0):
        """Document for access and update attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """Document for property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Document Property setter to set new size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Document for area of size"""
        return self.__size ** 2
