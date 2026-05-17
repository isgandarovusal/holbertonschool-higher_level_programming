#!/usr/bin/python3
"""Module that contains a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
