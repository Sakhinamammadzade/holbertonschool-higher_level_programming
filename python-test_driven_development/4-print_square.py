#!/usr/bin/python3
"""
square_printer_module

This module provides a function for printing a square pattern of '#' characters

"""


def print_square(size):
    """
        Print a square pattern of '#' characters.

        Parameters:
            size (int): The size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print("#" * size)
