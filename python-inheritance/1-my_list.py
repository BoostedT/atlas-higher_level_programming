#!/usr/bin/python3
"""Module that defines a custom list class with additional methods."""

class MyList(list):
    """Custom list class with additional methods.
    """

def print_sorted(self):
    """Prints the list, in ascending order by value."""
    if issubclass(MyList, list):
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")

MyList.print_sorted = print_sorted
