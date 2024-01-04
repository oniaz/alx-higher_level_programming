#!/usr/bin/python3
""" task 1 """


def write_file(filename="", text=""):
    """Writes a given text into a given file

        Args:
            filename (str): The path to the file to be read.
            text (str): The text to be written into the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
