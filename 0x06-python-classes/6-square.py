#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.
        Args:
            size (int): The size of the square. Defaults to 0.
                Raises a TypeError if size is not an integer.
                Raises a ValueError if size is less than 0.
            position (tuple): The position of the square. Defaults to (0, 0).
                Raises a TypeError if position is not a tuple of 2 positive integers. """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.
        Returns:
            int: The size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the square.
        Args:
            value (int): The size of the square.
                Raises a TypeError if value is not an integer.
                Raises a ValueError if value is less than 0. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieves the position of the square.
        Returns:
            tuple: The position of the square. """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.
        Args:
            value (tuple): The position of the square.
                Raises a TypeError if value is not a tuple of 2 positive integers."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """If size is equal to 0, prints an empty line.
        Considers the position when printing the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

