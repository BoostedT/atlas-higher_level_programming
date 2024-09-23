#!/usr/bin/python3
"""Module that defines a rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with given width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for i in range(self.height)])

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with width == height == size"""
        return cls(size, size)
