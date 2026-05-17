#!/usr/bin/env python3
"""
Module for basic serialization of a dictionary to JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserializes a JSON file to a Python dictionary.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
