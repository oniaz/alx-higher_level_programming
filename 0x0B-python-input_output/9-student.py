#!/usr/bin/python3
""" task 9 """


class Student:
    """ Represents a student with basic information.

        Methods:
            __init__
            to_json
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes a new instance of the Student class. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance.

            Returns:
                dict: A dictionary representation of the Student instance.
        """
        return self.__dict__
