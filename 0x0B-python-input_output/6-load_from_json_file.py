#!/usr/bin/python3
""" task 6 """


def load_from_json_file(filename):
    """creates an Object from a JSON file.

        Args:
            filename (str) : path to the JSON file.

        Returns:
            object: The loaded object from the JSON file.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
