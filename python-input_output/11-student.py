#!/usr/bin/python3
""" script that loads a list of students from a JSON file,
and then saves it to a new JSON file """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialize a new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return the dictionary representation of a Student """
        if attrs is None:
            return self.__dict__
        return {k: self.__dict__[k] for k in attrs if k in self.__dict__}

    def reload_from_json(self, json):
        """ Reloads the student information from a JSON object """
        for key, value in json.items():
            setattr(self, key, value)
