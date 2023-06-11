#!/usr/bin/python3

"""
identation module defined
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']

    for char in characters:
        text = text.replace(char, char + '\n\n')

    print(text.rstrip())
