#!/usr/bin/python3
"""
Define the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        """
        self.width = value
        self.height = value
