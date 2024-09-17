#!/usr/bin/python3
"""
This module contains a base geometry class.
"""


class BaseGeometry:
    """
    A base geometry class.
    """

    def __init__(self):
        """Initializes the base geometry class."""
        pass


    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")
    
    
    def integer_validator(self, name, value):
        """Validates the value as an integer.

        Args:
            name: The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
