#!/usr/bin/python3
"""Task 0 of ALX Project(Python - Inheritance)

This module defines an object attribute lookup function.

"""


def lookup(obj):
    """Check for an object's available attributes.

    Args:
        obj: the object

    Returns:
        list: available methods and attributes of the object.

    """
    return dir(obj)
