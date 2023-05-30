#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square. Defaults to 0.
                Raises a TypeError if size is not an integer.
                Raises a ValueError if size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.
        Returns:
            int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
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
            int: The area of the square.
        """
        return self.__size ** 2
