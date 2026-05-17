#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes,
including properties, setters, area, and a print method.
"""


class Square:
    """
    Defines a square by size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): The size of the square.
            position (tuple): The coordinates (horizontal, vertical).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # considering position."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
