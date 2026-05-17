#!/usr/bin/python3
""" Roman to Integer module """


def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for ch in roman_string:
        value = roman_dict.get(ch, 0)
        if prev < value and prev != 0:
            total -= 2 * prev

        total += value
        prev = value

    return total
