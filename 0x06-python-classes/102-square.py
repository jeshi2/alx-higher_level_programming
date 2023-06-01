#!/usr/bin/python3
"""defined square class"""


class Square:
    """square class rep"""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
            size (number): The size of the square. Defaults to 0.
                Raises a TypeError if size is not a number.
                Raises a ValueError if size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (number): The size of the square.
                Raises a TypeError if value is not a number.
                Raises a ValueError if value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of this square is equal to the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Checks if the area of this square is not equal to the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Checks if the area of this square is less than the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of this square is less than or equal to the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is less or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of this square is greater than the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of this square is greater than or equal to the area of another square.
        Args:
            other (Square): The other square to compare with.
        Returns:
            bool: True if this square's area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
