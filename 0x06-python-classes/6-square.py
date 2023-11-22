#!/usr/bin/python3
""" le task 4 """


class Square:
    """ defining le square """
    def __init__(self, size=0, position=(0, 0)):
        """ le square initialization

        Args:
            size(int): le square size
            position(int, int): le square position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ retrieves le square size """
        return self.__size

    @property
    def position(self):
        """ retrieves le square position """
        return self.__position

    @size.setter
    def size(self, value):
        """ sets le square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ sets le square size """
        if not isinstance(value, tuple) or not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value

    def area(self):
        """ returns le area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ some method to print some dumbass inaccurate
        representation of le useless square
        """
        if self.size > 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
        else:
            print()
