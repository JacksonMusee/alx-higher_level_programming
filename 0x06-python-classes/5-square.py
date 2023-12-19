#!/usr/bin/python3
"""
More classes
"""


class Square:
    """
    First class everything
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        size = self.size

        if size == 0:
            print("")
        else:
            for i in range(0, size):
                print("#" * size)
