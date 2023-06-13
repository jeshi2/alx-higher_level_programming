#!/usr/bin/python3
"""module write
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write (optional).
        text (str): The string to write to the file (optional).

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
