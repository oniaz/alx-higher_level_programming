#!/usr/bin/python3
""" task 7
    This script adds all passed arguments to a Python list,
    then saves the list to a file.
"""


if __name__ == "__main__":
    from sys import argv
    load_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    try:
        jsonlist = load_json_file(filename)
    except FileNotFoundError:
        jsonlist = []
    jsonlist.extend(argv[1:])
    save_to_json_file(jsonlist, filename)
