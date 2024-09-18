#!/usr/bin/python3
""" function that returns an object (Python data structure)
represented by a JSON string """

import json


def from_json_string(json_string):
    """
    Function that returns an object (Python data structure) represented by a JSON string.

    Args:
        json_string (str): A JSON string

    Returns:
        dict: A Python dictionary representing the JSON object
    """
    return json.loads(json_string)
