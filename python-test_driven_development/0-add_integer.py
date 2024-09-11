#!/usr/bin/python3
"""
module 0-add_integer
"""


def add_integer(a, b=98):
    """
    returns the sum of a and b
    float arguments are typecasted to ints before addition is performed
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
