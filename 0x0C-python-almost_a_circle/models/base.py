#!/usr/bin/python3
"""define class base
"""
import json

class Base:
    """
    Base class to manage id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional. The id value to assign.

        Attributes:
            id (int): The unique identifier of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes objects to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("")
            else:
                csv_data = [obj.to_csv() for obj in list_objs]  
                file.write("\n".join(csv_data))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a file in CSV format"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                csv_data = file.read().splitlines()
                instances = [cls.from_csv(line) for line in csv_data]
                return instances
        except FileNotFoundError:
            return []
