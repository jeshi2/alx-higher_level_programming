#!/usr/bin/python3
"""square module continue"""


class Square:
    """class for square creation"""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square. Defaults to 0.
                Raises a TypeError if size is not an integer.
                Raises a ValueError if size is less than 0."""
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square.
                Raises a TypeError if value is not an integer.
                Raises a ValueError if value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        Returns:
            int: The area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
