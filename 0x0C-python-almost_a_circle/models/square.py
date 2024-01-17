#!/usr/bin/python3

"""
Write the class Square that inherits from Rectangle:

Square is a special Rectangle, so it makes sense this class Square
inherits from Rectangle.
"""

from . import rectangle


class Square(rectangle.Rectangle):
    """
    Implementation of class square as required above
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of an abject
        """
        super().__init__(size, size, x=x, y=y, id=None)

    def __str__(self):
        """
        Return a strng represention
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
