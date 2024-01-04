#!/usr/bin/python3
""" task 0 """


def read_file(filename=""):
    """Prints the content of a given file

        Args:
            filename (str): The path to the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
