#!/usr/bin/python3
"""module read
"""

def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to read (optional).

    Returns:
        None

    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
