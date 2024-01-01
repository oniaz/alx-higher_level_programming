#!/usr/bin/python3
""" Task 9 module. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inheits from basegeomnety. boi i dont want want to documnet """

    def __init__(self, width, height):
        """ initializing the rectangle and setting its dimensions.

            Args:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculating and returning the area of the rectangle.

            Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Provides a description for the rectangle in the format:
                '[Rectangle] <width>/<height>'

            Returns:
                str: rectangle description with in the form
                    '[Rectangle] <width>/<height>'
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
