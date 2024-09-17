#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or an inherited class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or an inherited class,
        False otherwise.
    """
    return isinstance(obj, a_class)
