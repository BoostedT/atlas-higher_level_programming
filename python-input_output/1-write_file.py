#!/usr/bin/python3
""" writes a string to a text file and returns the number of characters written """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number of characters written """

    with open(filename, 'w') as f:
        return f.write(text)
