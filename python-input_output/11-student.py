#!/usr/bin/python3
"""
Module that defines a Student class with disk reload capabilities.
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
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys are attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
