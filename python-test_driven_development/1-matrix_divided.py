#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
All elements must be integers or floats.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
