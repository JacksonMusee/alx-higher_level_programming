#!/usr/bin/python3
"""
Of course we have to document this module
Our module contains only one functon
Procced to see the code
Test doc will be here tests/4-print_square.txt
"""


def print_square(size):
    """
    This functon prints a square of size by size
    Uses '#' to print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if not size >= 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")

    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()
