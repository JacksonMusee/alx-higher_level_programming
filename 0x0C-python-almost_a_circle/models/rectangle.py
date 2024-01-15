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
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

    def set_width(self, width):
        """
        A setter for prvate attribute__width
        """
        self.__width = width

    def get_width(self):
        """
        Returns the width of this instance
        """
        return self.__width

    def set_height(self, height):
        """
        Setter for private attribute __height
        """
        self.__height = height

    def get_height(self):
        """
        Getter for __height
        """
        return self.__height

    def set_x(self, x):
        """
        Setter for private attribute __x
        """
        self.__x = x

    def get_x(self):
        """
        Getter for __x
        """
        return self.__x

    def set_y(self, y):
        """
        Setter fo private attribute __y
        """
        self.__y = y

    def get_y(self):
        """
        Getter for __y
        """
        return self.__y
