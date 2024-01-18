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
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """
        Return a strng represention
        """

        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set size by allocating it's value to width and height
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Assigns attributes from args and kwargs
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])
