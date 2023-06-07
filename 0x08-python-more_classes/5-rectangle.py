#!/usr/bin/python3

"""class rectangle
"""


class Rectangle:
    """an empty class
    """

    def __init__(self, width=0, height=0):
        """initilz class rctangle
        """
        self.width = width
        self.height = height

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
        """set height sstter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rect
        """
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return string rep of rectanle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """return represnt of rec that can be used in eval() to create object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del instance of rectangle class
        """
        print("Bye rectangle...")
