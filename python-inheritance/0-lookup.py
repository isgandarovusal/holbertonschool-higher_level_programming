#!/usr/bin/python3
"""
This module defines a lookup function.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
