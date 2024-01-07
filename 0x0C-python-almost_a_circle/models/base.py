#!/usr/bin/python3
""" task 1 - Base Class"""


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
