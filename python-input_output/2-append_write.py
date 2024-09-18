#!/usr/bin/python3
""" appends a string at the end of a text file and
returns the number of characters added """

def append_write(filename, text):
    """ appends a string at the end of a text file and
    returns the number of characters added """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
