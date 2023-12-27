#!/usr/bin/python3
def lookup(obj = None):
	"""Returns the list of available attributes and methods of an object.

	Args:
		obj (object): The object for which a list will be returned with its attributes and methods.

	Returns:
		list: A list of the attributes and methods of the provided object.
	"""
	return dir(obj)