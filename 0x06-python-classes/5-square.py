#!/usr/bin/python3
""" le task 4 """


class Square:
    """ defining le square """
    def __init__(self, size=0):
        """ le square initialization

        Args:
            size(int): le square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ retrieves le square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets le square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns le area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ some method to print some dumbass inaccurate
        representation of le useless square
        """
        if self.size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
