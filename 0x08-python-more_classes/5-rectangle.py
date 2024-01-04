#!/usr/bin/python3
"""
A simple module about classes
With only one class
"""


class Rectangle:
    """
    One simple class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            peri = 0
        else:
            peri = (self.width + self.height) * 2

        return peri

    def __str__(self):
        return self.print_rec()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        del self

    def print_rec(self):
        rec = ''
        if self.width == 0 or self.height == 0:
            return rec
        else:
            for x in range(0, self.height - 1):
                rec += ("#" * self.width) + '\n'
            rec += ("#" * self.width)
            return rec
