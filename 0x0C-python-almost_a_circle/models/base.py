#!/usr/bin/python3
""" Base Class"""


import json


class Base:
    " Base Class. maganes id attribute for all subclasses"
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing the base instance by assigning an id

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
        """ Returns the JSON string representation of the passed dictionary."""
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of the given list object to
            a json file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                thelist = []
                for obj in list_objs:
                    thelist.append(cls.to_dictionary(obj))
                file.write(Base.to_json_string(thelist))
                # json.dump(thelist, file)
