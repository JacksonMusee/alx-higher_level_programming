#!/usr/bin/python3
"""
Module is documented Classes are fun
"""


class Square:
    """
    A square class or type doing many things
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif (value < 0):
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) or \
                not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        a = self.size ** 2
        return a

    def my_print(self):
        size = self.size
        position = self.position

        if size == 0:
            print("")

        else:
            if position[1] > 0:
                print("")

            for i in range(0, size):
                print((" " * position[0]) + ("#" * size))
