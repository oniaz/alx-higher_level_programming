#!/usr/bin/python3
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
