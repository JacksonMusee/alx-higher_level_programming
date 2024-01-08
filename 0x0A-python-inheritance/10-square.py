#!/usr/bin/python3
"""
Module
"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    We are bundling a square and all operation together
    Get to the code
    """

    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
