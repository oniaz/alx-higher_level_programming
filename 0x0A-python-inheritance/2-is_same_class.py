#!/usr/bin/python3
""" Task 2 module.
    This module provides a function that checks if a given instance is of a
    specified class.
"""


def is_same_class(obj, a_class):
    """checks if a given instance is of a specified class.

    Args:
        obj (object): The object to be checked
        class (a_class): the class

    Returns:
        Boolean: True if the object is exactly an instance of the specified
        class; otherwise, False.
    """
    return type(obj) is a_class
