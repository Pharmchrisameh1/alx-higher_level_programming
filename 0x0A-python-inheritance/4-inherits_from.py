#!/usr/bin/python3
"""Task 4 of ALX Project(Python - Inheritance)

This module defines a function that confirms an object-class relationship.

"""


def inherits_from(obj, a_class):
    """Check if the specified object is an instance of
    a class that inherited directly or indirectly from
    the specified class.

    Args:
        obj: the object
        a_class: the class

    Returns:
        bool: True, if there's such a relationship, and False, if otherwise.

    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
