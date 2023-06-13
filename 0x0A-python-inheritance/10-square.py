#!/usr/bin/python3
"""more base class
"""
Rectangle = __import__('9-rectangle').Rectangle

"""module square
"""

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.
        Size must be a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
