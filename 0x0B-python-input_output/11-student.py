#!/usr/bin/python3
""" task 11 """


class Student:
    """ Represents a student with basic information.

        Methods:
            __init__
            to_json
            reload_from_json
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

    def reload_from_json(self, json):
        """ Updates/adds the values provided in the passed dictionary to the
            instance attributes.

        Args:
            json (dict): A dictionary with the attributes and the values that
                        shall be replaced for the Student instance with their
                        values.
        """
        for key in json:
            setattr(self, key, json[key])
