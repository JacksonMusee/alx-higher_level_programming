#!/usr/bin/python3
from magic_calculation_102 import add
from magic_calculation_102 import sub


def magic_calculation(a, b):
    if (a < b):
        c = add(a, b)

    else:
        return a + b

    for i in range(4, 6):
        c = add(c, i)

    return c
