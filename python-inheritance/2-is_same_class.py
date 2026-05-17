#!/usr/bin/python3
"""
This module defines a function that checks for an exact class instance.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
