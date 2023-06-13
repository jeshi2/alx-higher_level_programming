#!/usr/bin/python3
"""module BaseGeometry (Parent)
"""

class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.
        Raises TypeError if value is not an integer,
        and ValueError if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""module that inherit from BaseGeometry
"""

class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.
        Width and height must be positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
