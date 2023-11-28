#!/usr/bin/python3
"""A module representing a square """


class Square:
    """A class representing a square """

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square its size.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
