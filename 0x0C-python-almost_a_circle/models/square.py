#!/usr/bin/python3
"""A module representing a square. """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class. A subclass of Rectangle class. """

    def __init__(self, size=0, x=0, y=0, id=None):
        """ initializing the square instance.

            Args:
                size (int): the length of a side of the square.
                x (int): x coordinate.
                y (int): y coordinate.
                id (int): the instance id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string with the square attributes values. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
        - value (int): The value of size.
        """
        Rectangle.int_validator("width", value)
        Rectangle.dimensions_validator("width", value)
        self.width = value
        self.height = value
        # super().width(value)
        # super().height(value)
