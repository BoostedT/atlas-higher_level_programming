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

    def to_json(self):
        """ Return the dictionary representation of a Student """
        return self.__dict__
