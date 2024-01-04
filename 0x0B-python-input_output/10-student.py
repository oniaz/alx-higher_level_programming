#!/usr/bin/python3
""" task 10 """


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

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance with
            attributes provided in the passed list. If no list is provided,
            all attributes are retrieved.

            Args:
                attrs (list): a list of the attributes to be retrieved.

            Returns:
                dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        description = {}
        for attr in attrs:
            try:
                description[attr] = getattr(self, attr)
            except AttributeError:
                pass
        return description
