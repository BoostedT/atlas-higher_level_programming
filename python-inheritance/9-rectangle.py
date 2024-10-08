#!/usr/bin/python3
""" This module defines a Rectangle class that inherits from BaseGeometry. """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ initializes the width and height of the rectangle. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ returns a string representation of the rectangle. """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
