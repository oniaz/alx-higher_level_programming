#!/usr/bin/python3
""" Task 2 module.
    This module provides a function that checks if a given instance is of a 
    specified class or one of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """checks if a given instance is of a specified class or one of its
       subclasses.

    Args:
        obj (object): The object to be checked
        class (a_class): the class

    Returns:
        bool: True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class;
        otherwise, False.
    """
    return isinstance(obj, a_class)
