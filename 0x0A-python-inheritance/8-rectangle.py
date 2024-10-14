#!/usr/bin/python3
"""Task 8 of ALX Project(Pythin - Inheritance)

This module defines a class that inherits from another class.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
