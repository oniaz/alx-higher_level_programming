#!/usr/bin/python3
""" task 3 """


def to_json_string(my_obj):
    """ Returns the JSON representation of an object.

        Args:
            my_obj: The object to be converted to a JSON string.

        Returns:
            str : the JSON representation of the input object.
    """
    import json
    return json.dumps(my_obj)
