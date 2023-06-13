#!/usr/bin/python3
"""module add attribute
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Arguments:
    - obj: The object to which the attribute should be added.
    - attribute: The name of the attribute.
    - value: The value of the attribute.

    Raises:
    - TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
