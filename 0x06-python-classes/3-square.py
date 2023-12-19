#!/usr/bin/python3
"""
Documentation goes here but we not doing that now
"""


class Square:
    """
    Square class working
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
