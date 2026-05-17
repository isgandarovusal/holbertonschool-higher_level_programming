#!/usr/bin/python3
"""
This module provides a function that indents text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Flag to skip spaces at the start of a new line
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in ".?:":
            print("\n")
            skip_space = True
