#!/usr/bin/python3
""" task 8 """


def class_to_json(obj):
    """Returns the dictionary description with simple data structures (list,
        dictionary, string, integer and boolean) for the JSON serialization of
        an object.

    Args:
        obj (object): The object for which a dictionary representation will be
                      returned.

    Returns:
        dict: Dictionary representation of the given object with its
              serializable attributes.
    """
    return obj.__dict__
