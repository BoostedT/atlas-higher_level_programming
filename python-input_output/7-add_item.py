#!/usr/bin/python3
""" adds all items to a Python list and saves them to a file """

import sys
import json


def add_item(my_list, item):
    """ adds an item to a list """
    my_list.append(item)
    return my_list

def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a JSON file

    Args:
        filename (str): name of the JSON file
        obj (object): object to be written
    """
    with open(filename, "w") as f:
        filename = f.write(json.dumps(my_obj))
    return filename

def load_from_json_file(filename):
    """ function that creates an Object from a JSON file

    Args:
        filename (str): name of the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
