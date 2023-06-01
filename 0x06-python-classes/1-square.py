#!/usr/bin/python3
"""square that set size as private instance variable"""


class Square:
    """ creation of square"""

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): the size of the square
        """
        self.__size = size
