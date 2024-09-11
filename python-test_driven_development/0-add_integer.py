#!/usr/bin/python3
"""
module 0-add_integer
"""


def add_integer(a, b=98):
    """
    adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        the addition of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
