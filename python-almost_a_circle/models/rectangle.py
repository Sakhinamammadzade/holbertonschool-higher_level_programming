#!/usr/bin/python3
"""Fisrt Rectangle"""

from models.base import Base


class Rectangle(Base):
    """"Define a new class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method fo r width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """prop for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """prop for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle with the character #"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__width,
                self.__height,
                self.__x,
                self.__y))
