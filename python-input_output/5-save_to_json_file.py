#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a JSON file

    Args:
        filename (str): name of the JSON file
        obj (object): object to be written
    """
    with open(filename, "w") as f:
        filename = (json.dumps(my_obj))
    return filename
