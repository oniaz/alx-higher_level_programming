#!/usr/bin/python3
""" task 3 or whatever """


class Square:
    """ some square that does stuff. """
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

    def area(self):
        """ returns the area of the square """
        return self.__size * self.__size
