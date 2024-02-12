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
    def width(self, x):
        """Setter method for width property"""
        self.__width = x


    @property
    def height(self):
        """Property for height"""
        return self.__height

    @height.setter
    def height(self, y):
        """Setter method for height property """
        self.__height = y

