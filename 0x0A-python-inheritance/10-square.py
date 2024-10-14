#!/usr/bin/python3
"""Task 10 of ALX Project(Pythin - Inheritance)

This module defines a class that inherits from another class.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the Square

        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Find the area of a Square"""
        return self.__size ** 2
