#!/usr/bin/python3
"""Real definition of a rectangle."""


class Rectangle:
    "Define a Rectangle class"
    def __init__(self, width=0, height=0):
        """Function for access and update attribute"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height property """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function returns perimetr of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Should print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""

        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """should return a string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
