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