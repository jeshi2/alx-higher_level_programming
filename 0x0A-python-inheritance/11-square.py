#!/usr/bin/python3
"""module class
"""

Rectangle = __import__('9-rectangle').Rectangle

"""modified square class
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
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
