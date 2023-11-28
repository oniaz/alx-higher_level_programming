#!/usr/bin/python3
"""A module representing a square """


class Square:
    """A class representing a square """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
        - value (int): The value to be set as the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            (int, int): the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
        - value ((int, int)): The value to be set as the position of
        the square.
        """
        if (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] > 0 and value[1] > 0):
            self.__size = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates and returns the area of the square its size.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout a representation of the square using the
        '#'character.If the size of the square is equal to 0, an
        empty line is printed.
        """
        if self.__size > 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
        else:
            print()
