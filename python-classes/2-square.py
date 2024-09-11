#!/usr/bin/python3

"""
This is a module that defines a square
"""


class Square:
    """
    This is a class that defines a square
    """
    def __init__(self, size):
        """
        This is a method that initializes the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
