#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
                Raises a TypeError if size is not an integer.
                Raises a ValueError if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
