#!/usr/bin/python3
"""function that returns list
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
