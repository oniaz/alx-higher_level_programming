#!/usr/bin/python3
""" Task 1 module.
	This module provides a lookup function to retrieve a list of attributes and methods associated with an object.
"""


def lookup(obj = None):
	"""Returns the list of available attributes and methods of an object.

	Args:
		obj (object, optional): The object for which a list will be returned with its attributes and methods.

	Returns:
		list: A list of the attributes and methods of the provided object.
	"""
	return dir(obj)