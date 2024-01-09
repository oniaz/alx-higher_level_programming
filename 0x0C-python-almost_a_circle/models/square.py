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

    def update(self, *args, **kwargs):
        """ Updates the attributes of a square instancw. Values can be passed
            either as positional arguments (args) or with their attribute names
            as keyword arguments (kwargs).

            Args:
                *args: Positional arguments representing values to be updated.
                        Must be in the order: "id", "size", "x", "y"

                **kwargs: Keyword arguments representing attribute names and
                        their alues.
        """
        attributes = ["id", "size", "x", "y"]
        if len(args) > 0:
            try:
                for i in range(len(args)):
                    setattr(self, attributes[i], args[i])
            except (IndexError):
                pass
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a square instance with
            the attributes: id, x, size, y
        """
        attributes = ["id", "x", "size", "y"]
        description = {}
        for attr in attributes:
            description[attr] = getattr(self, attr)
        return description
