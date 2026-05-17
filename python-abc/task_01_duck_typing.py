#!/usr/bin/env python3
"""
Module for Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a Shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter."""
        pass


class Circle(Shape):
    """Class representing a Circle."""

    def __init__(self, radius):
        """Initialize the Circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        """Return the area of the Circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the Circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
