#!/usr/bin/python3imp
""" Task 11 module. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inheits from wecangle. boi i dont want want to documnet """

    def __init__(self, size):
        """ initializing the square and setting its size.

            Args:
                size (int): the length of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Provides a description for the square in the format:
                '[Square] <size>/<size>'

            Returns:
                str: square description with in the form of
                    '[Square] <size>/<size>'
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
