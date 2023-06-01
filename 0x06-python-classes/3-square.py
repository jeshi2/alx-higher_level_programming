#!/usr/bin/python3
"""square module continue"""


class Square:
    """square class creation"""
    
    def __init__(self, size=0):
       """set size to private instance variable

       Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
       """get area of a square

       Args:
           NOne

        Returns:
            Area of square(int)
        """
        return self.__size ** 2
