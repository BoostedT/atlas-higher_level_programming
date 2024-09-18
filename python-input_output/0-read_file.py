#!/usr/bin/python3
def read_file(filename=""):
    """ reads a text file and prints it to stdout """

    with open(filename) as f:
        text = f.read()
        print(text, end="")
