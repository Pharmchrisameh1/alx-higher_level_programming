#!/usr/bin/python3
"""Task 11 of ALX Project(Pythin - Inheritance)

This module defines a class that inherits from another class.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new Square based on a Rectangle.

        Args:
            size (int): The size of the new Square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of a Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
