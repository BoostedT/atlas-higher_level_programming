#!/usr/bin/python3
"""defines a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.
        Defaults to an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
