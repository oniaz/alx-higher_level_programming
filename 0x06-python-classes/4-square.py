#!/usr/bin/python3
""" task 4 or whatever """


class Square:
    """ some square class that does stuff. """
    def __init__(self, size=0):
        """ square initialization

        Args:
            size(int): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """ retrieves the square size """
        return self.__size

    def size(self, value):
        """ sets the square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the square """
        return self.__size * self.__size
