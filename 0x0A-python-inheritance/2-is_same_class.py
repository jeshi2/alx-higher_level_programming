#!/usr/bin/python3
"""a function that returns True
  if the objects is exctly an instance
  of the specified class
  """

def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class;
    otherwise, returns False.
    """
    return type(obj) is a_class
