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

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance"""
        if args and len(args) > 0:
            attr_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,  # Since width and height are the same in Square
            "x": self.x,
            "y": self.y
        }
