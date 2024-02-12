#!/usr/bin/python3
"""Fisrt Rectangle"""

from models.base import Base


class Rectangle(Base):
    """"Define a new class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method fo r width property"""
        self.__width = width

    @property
    def height(self):
        """Property for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height property """
        self.__height = height

    @property
    def x(self):
        """prop for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @property
    def y(self):
        """prop for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y
