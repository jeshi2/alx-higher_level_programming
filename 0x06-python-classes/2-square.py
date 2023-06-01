#!/usr/bin/python3
"""square module"""


class Square:
    """class for square"""

    def __init__(self, size=0):
        """
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
