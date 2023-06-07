#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """an empty class defined
    """

    def __init__(self, width=0, height=0):
        """method: __int__ init instance of rec"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """med: set_width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """method: set_height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        """calculate area of a rectangle"""

    def area(self):
        return self.__width * self.__height
    """calculate perimeter of rectangle"""

    def perimeter(self):
        return 2 * (self.__width + self.__height)

