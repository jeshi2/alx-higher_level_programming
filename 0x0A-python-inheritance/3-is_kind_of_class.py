#!/usr/bin/python3
"""function return true if object is an instance
    or otherwise false
    """

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or if it is an instance of
    a class that inherited from a_class; otherwise, returns False.
    """
    return isinstance(obj, a_class)
