#!/usr/bin/python3
"""
This module has one function
Which willdivide all number in a matrix
Return a new matrix
The old one remains unchanged
"""


def matrix_divided(matrix, div):
    """
    Everything done here has been explained
    There is also a separate docs
    """

    new_matrix = []
    msg = '(list of lists) of integers/floats'

    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(f'matrix must be a matrix {msg}')

        for i in item:
            if not isinstance(i, int) and not isinstance(div, float):
                raise TypeError(f'matrix must be a matrix {msg}')

        if len(item) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(0, len(matrix)):
        new_matrix.append([])

        for j in range(0, len(matrix[0])):
            num = matrix[i][j]
            new_matrix[i].append(round((num / div), 2))

    return new_matrix
