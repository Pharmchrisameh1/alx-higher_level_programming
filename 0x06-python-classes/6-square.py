#!/usr/bin/python3
"""Task 6 of ALX Project(Python - Classes and Objects)

This module defines a class.

"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Default to 0
            position (tuple, optional): Represents the position of the square

        """

        self.__size = size
        self.__position = (0, 0)
        if position != (0, 0):
            self.position = position

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/Set the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not(isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the current area of the square

        Returns:
            Area of square

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
