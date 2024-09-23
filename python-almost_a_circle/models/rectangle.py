#!/usr/bin/python3
"""Module that defines a rectangle"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        self.validate_int("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        self.validate_int("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Returns the x value of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Sets the x value of the rectangle"""
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns the y value of the rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle"""
        self.validate_int("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
    
    def display(self):
        """Displays the rectangle"""
        print(f"Rectangle {self.id} at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def to_dict(self):
        """Returns a dictionary representation of the rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
