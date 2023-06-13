#!/usr/bin/python3
"""append module
"""

def append_write(filename="", text=""):
    """
    Append a string at the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the file to append (optional).
        text (str): The string to append to the file (optional).

    Returns:
        int: The number of characters added.

    """
    with open(filename, mode="a", encoding="utf-8") as file:
        num_chars = file.write(text)
    return num_chars
