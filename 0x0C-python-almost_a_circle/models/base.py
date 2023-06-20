#!/usr/bin/python3
"""define class base
"""

class Base:
    """
    Base class to manage id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional. The id value to assign.

        Attributes:
            id (int): The unique identifier of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

