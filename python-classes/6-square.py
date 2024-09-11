#!/usr/bin/python3

"""
module for printing a square
"""


class Square:
    """
    class square
    """

    def __init__(self, size=0):
        """
        init method
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
