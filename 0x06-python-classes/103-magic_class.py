#!/usr/bin/python3
"""interpreted a python class code bytecode"""

import math


class MagicClass:
    """magiclass decode"""

    def __init__(self, radius=0):
        """init class of magicclass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calc area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calc the circumference"""
        return 2 * math.pi * self.__radius
