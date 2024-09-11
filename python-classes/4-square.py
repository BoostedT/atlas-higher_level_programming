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
        Initialize a Square.

        Parameters:
        size (int, optional): The side length of the square. Defaults to 0.
        """
        self.__size = size
        self.my_print()

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        value (int): The new size of the square.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This is a method that returns the area of the square
        """
        return (self.__size * self.__size)
