#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        if not list_:
            print()
            exit()

    for i in range(len(matrix)):
        for element in matrix[i]:
            if element == matrix[i][-1]:
                print("{:d}".format(element))
            else:
                print("{:d} ".format(element), end="")
