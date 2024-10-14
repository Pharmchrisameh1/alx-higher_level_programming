#!/usr/bin/python3
"""Task 7 of ALX Project(Python - Inheritance)

This module defines a class that just does random things.

"""


class BaseGeometry:
    """Do some few things"""

    def area(self):
        """Raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is an integer.

        Args:
            name: any name at all
            value (int): the value to be validated

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less than or equal to 0

        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
