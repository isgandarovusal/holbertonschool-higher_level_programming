#!/usr/bin/python3
"""
Module that defines a Student class with filter.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained
        in this list are retrieved.

        Args:
            attrs (list): A list of strings representing attribute names.

        Returns:
            dict: The dictionary representation of the student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
