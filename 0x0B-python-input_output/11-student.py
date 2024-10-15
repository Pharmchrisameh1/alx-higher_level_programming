#!/usr/bin/python3
"""Task 11 of ALX Project(Python - Input/Output)

This module defines a student class.

"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.

        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {attr: self.__dict__.get(attr) for attr in attrs
                    if attr in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of a Student.

        Args:
            json (dict): The attributes:values to replace attributes with

        """
        for key, value in json.items():
            setattr(self, key, value)
