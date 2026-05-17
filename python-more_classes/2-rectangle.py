#!/usr/bin/python3
"""
This module defines a Rectangle class with area and perimeter methods.
"""


class Rectangle:
    """
    Defines a rectangle by width and height, and calculates area and perimeter.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
