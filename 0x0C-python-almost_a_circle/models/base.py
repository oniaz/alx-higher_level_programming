#!/usr/bin/python3
""" Base Class"""


import json


class Base:
    """ The base class. Assigns the id attribute for all subclasses. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the base instance by assigning an id.The ID can be
            passed or auto-incremented.

            Args:
                id (int): the instance id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Serializes a given list (of dictionaries) into a JSON string.

            Args:
                list_dictionaries (list): a list of dictionaries.

            Returns:
                str: the JSON string representation of the list.

        """
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Given a list of instances of a class, for each instance, a
            dictionary is generated containing its attribute values. These
            dictionaries are then placed in a list and serialized into a JSON
            string, which is then saved to a JSON file with the name of the
            class.

            Args:
                list_objs (list): a list of instances for a class.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                thelist = []
                for obj in list_objs:
                    thelist.append(cls.to_dictionary(obj))
                # instead of json.loads()
                file.write(Base.to_json_string(thelist))

    @staticmethod
    def from_json_string(json_string):
        """ Deserializes a JSON string into a list.

            Args:
                json_string (str): a json string.

            Returns:
                obj: the deserialization of the json string or an empty
                    list if no json string was passed.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with given attributes.

            Args:
                **dictionary(): attribute-value pairs for different instance
                                attributes.

            Returns:
                obj: the newly created instance.
        """
        if cls.__name__ == "Rectangle":
            if ("width" not in dictionary) and ("height" not in dictionary):
                new_instance = cls()
            if ("width" not in dictionary):
                new_instance = cls(height=1)
            if ("height" not in dictionary):
                new_instance = cls(width=1)
            new_instance = cls(1, 1)

        elif cls.__name__ == "Square":
            if ("size" not in dictionary):
                new_instance = cls()
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Creates new instances of the class using instance attributes saved
            in a json file with the class name.

            Returns:
                list: a list of the newly created instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                attr_list = Base.from_json_string(file.read())
            instance_list = []
            for instance in attr_list:
                instance_list.append(cls.create(**instance))
            return instance_list
        except (FileNotFoundError):
            return []
