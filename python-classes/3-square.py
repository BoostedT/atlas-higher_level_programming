#!/usr/bin/python3

"""
This is a module that defines a square
"""


class Square:
    """
    This is a class that defines a square
    """
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Parameters:
        size (int, optional): The side length of the square. Defaults to 0.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This is a method that returns the area of the square
        """
        return (self.__size * self.__size)
