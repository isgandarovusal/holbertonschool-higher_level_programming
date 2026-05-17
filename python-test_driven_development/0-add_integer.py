#!/usr/bin/python3
"""
This module provides a function that adds two integers.
Inputs must be integers or floats that can be cast to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    Raises TypeError if inputs are not integers, floats, or are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN is the only value that does not equal itself
    # abs(x) == inf checks for both positive and negative infinity
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
