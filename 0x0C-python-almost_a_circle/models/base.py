#!/usr/bin/python3
"""define class base
"""
import json
import csv
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
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj_dict['id'], obj_dict['width'],
                                obj_dict['height'], obj_dict['x'], obj_dict['y']])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj_dict['id'], obj_dict['size'],
                            obj_dict['x'], obj_dict['y']])

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
        obj_list = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj_dict = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                        obj = cls.create(**obj_dict)
                        obj_list.append(obj)
                    elif cls.__name__ == "Square":
                        obj_dict = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                        obj = cls.create(**obj_dict)
                        obj_list.append(obj)
        except FileNotFoundError:
            return []
        return obj_list
