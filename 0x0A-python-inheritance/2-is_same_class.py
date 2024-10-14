#!/usr/bin/python3
"""Task 2 of ALX Project(Python - Inheritance)

This module defines a function that confirms an object-class relationship.

"""


def is_same_class(obj, a_class):
    """Check if the specified object is exactly an instance of
    the specified class.

    Args:
        obj: the object
        a_class: the class

    Returns:
        bool: True, if there's a direct relationship, and False, if otherwise.

    """
    if type(obj) == a_class:
        return True
    else:
        return False
