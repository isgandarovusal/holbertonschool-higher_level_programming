#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements are of type int.
        """
        print(sorted(self))
