#!/usr/bin/python3
""" function that returns the dictionary description
with simple data structure for JSON serialization of an object """

import json

def dict_description(obj):
    """Function that returns the dictionary description
    with simple data structure for JSON serialization of an object

    Args:
        obj (object): object to be serialized
    """
    return obj.__dict__
