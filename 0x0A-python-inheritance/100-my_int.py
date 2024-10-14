#!/usr/bin/python3
"""Task 12 of ALX Project(Python - Inheritance)

This module defines a class that inherits the `int` class.

"""


class MyInt(int):
    """Invert operators == and !=."""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
