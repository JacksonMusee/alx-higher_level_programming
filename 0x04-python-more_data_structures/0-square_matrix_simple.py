#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in range(0, len(matrix)):
        new_matrix.append([])
        for j, v in enumerate(matrix[i]):
            new_element = matrix[i][j] ** 2
            new_matrix[i].append(new_element)
    return new_matrix
