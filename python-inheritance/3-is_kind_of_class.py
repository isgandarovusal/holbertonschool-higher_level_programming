#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance or inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
