#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """
    Implements the requirements above
    """
    power_count = 0
    i = 1
    main_list = []
    new_list = []

    while power_count < n:
        new_list.append(1)

        if main_list:
            last_list = main_list[-1]

            while True:
                try:
                    last_list[i]
                except IndexError:
                    new_list.append(1)
                    i = 1
                    break
                else:
                    new_list.append((last_list[i-1] + last_list[i]))
                    i += 1

        main_list.append(new_list)
        new_list = []
        power_count += 1

    return main_list
