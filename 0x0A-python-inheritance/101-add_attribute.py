#!/usr/bin/python3
"""Task 13 of ALX Project(Python - Inheritance)

This module defines a function that adds attributes to objects.

"""


def add_attribute(obj, attr, value):
    """Add an attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attr (str): The name of the attribute to be added.
        value (any): The value of attr.

    Raises:
        TypeError: if no attribute can be added to obj

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
