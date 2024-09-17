#!/usr/bin/python3
"""Module that defines a custom list class with additional methods."""

class MyList(list):
    """Custom list class with additional methods.
    """

def print_sorted(self):
    """Prints the list, in ascending order by value."""
    sorted_list = sorted(self)
    print(sorted_list)
