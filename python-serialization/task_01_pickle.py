#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickling."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a specific format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
