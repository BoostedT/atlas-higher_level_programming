#!/usr/bin/python3
""" Prints the current working directory and its contents. """


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; False otherwise.
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
