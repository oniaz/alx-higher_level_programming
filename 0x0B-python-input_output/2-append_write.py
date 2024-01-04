#!/usr/bin/python3
""" task 2 """


def append_write(filename="", text=""):
    """Appends a given text to a given file

        Args:
            filename (str): The path to the file to be read.
            text (str): The text to be appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
