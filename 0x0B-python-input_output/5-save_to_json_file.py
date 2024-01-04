#!/usr/bin/python3
""" task 5 """


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

        Args:
            my_obj: The object to be written to the file.
            filename (str) : path to the JSON file.
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
