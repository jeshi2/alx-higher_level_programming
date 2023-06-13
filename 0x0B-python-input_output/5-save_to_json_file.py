#!/usr/bin/python3
"""module save json file
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to save the JSON representation.

    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
