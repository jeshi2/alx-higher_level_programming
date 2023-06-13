#!/usr/bin/python3
"""module student
"""

class Student:
    """represent student
    """

    def __init__(self, first_name, last_name, age):
        """initialize a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive dict rep on instances
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
