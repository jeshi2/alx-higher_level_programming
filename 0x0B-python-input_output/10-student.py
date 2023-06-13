#!/usr/bin/python3
"""module student
"""

class Student:
    """
    Student class represents a student.

    Public instance attributes:
        first_name: First name of the student.
        last_name: Last name of the student.
        age: Age of the student.

    Methods:
        __init__(self, first_name, last_name, age):
            Initializes a new instance of the Student class.

        to_json(self, attrs=None):
            Retrieves a dictionary representation of a Student instance.

    Usage:
        student = Student(first_name, last_name, age)
        json_data = student.to_json(attrs)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name: First name of the student.
            last_name: Last name of the student.
            age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: Optional list of attribute names to retrieve.
                If provided, only the specified attributes will be included in the dictionary.
                If None (default), all attributes will be included.

        Returns:
            A dictionary containing the attribute names and their corresponding values.

         """
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
