#!/usr/bin/python3
"""json to class
"""

def class_to_json(obj):
    json_dict = {}

    # Get all attributes of the object
    attributes = obj.__dict__

    # Iterate over each attribute
    for attr, value in attributes.items():
        # Skip private attributes
        if attr.startswith("__"):
            continue

        # Check if the value is a list or dictionary
        if isinstance(value, (list, dict)):
            json_dict[attr] = value
        else:
            # Convert other data types to their JSON-compatible equivalents
            if isinstance(value, str):
                json_dict[attr] = value
            elif isinstance(value, int):
                json_dict[attr] = value
            elif isinstance(value, bool):
                json_dict[attr] = value

    return json_dict
