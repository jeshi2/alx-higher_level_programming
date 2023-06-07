#!/usr/bin/python3
"""class rectangle
"""


class Rectangle:
    """ class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """set width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return nice string rep
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """___repr___ create new objects
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del instances
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
