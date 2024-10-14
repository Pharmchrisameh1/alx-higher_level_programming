#!/usr/bin/python3
"""Task 3 of ALX Project(Python - Inheritance)

This module defines a function that confirms an object-class relationship.

"""


def is_kind_of_class(obj, a_class):
    """Check if the specified object is an instance of,
    or if it is an instance of a class that inherited from,
    the specified class.

    Args:
        obj: the object
        a_class: the class

    Returns:
        bool: True, if there's such a relationship, and False, if otherwise.

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
