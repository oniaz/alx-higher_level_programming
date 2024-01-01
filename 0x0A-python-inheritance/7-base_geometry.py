#!/usr/bin/python3
""" Task 7 module. """


class BaseGeometry():
    """ Base Class with an as-for-now a nonfunctioning area function.
        and an int validator function.
    """
    def area(self):
        """ Raises an error message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks if the value is a positive int """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (value < 1):
            raise ValueError(name + " must be greater than 0")
