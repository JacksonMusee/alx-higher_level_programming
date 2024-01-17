#!/usr/bin/python3

"""
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the
__init__ of the Base class
Assign each argument width, height, x and y to the right attribute
"""

from . import base


class Rectangle(base.Base):
    """
    See above docs from description
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an object of class Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the width of this instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        A setter for prvate attribute__width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """
        Getter for __height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter for private attribute __height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """
        Getter for __x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for private attribute __x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """
        Getter for __y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter fo private attribute __y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        print("\n" * self.y, end="")
        for line in range(self.height):
            print(f'{" " * self.x}{"#" * self.width}')

    def __str__(self):
        """
        Overriding the __str__ method so that it returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[{self.__class__.__name__}] "
                f"({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")
