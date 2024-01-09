#!/usr/bin/python3
""" Module representing a Rectangle """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class. A subclass of Base class. """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Initializing the rectangle instance.

            Args:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.
                x (int): x coordinate.
                y (int): y coordinate.
                id (int): the instance id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def int_validator(attribute_name, value):
        """ Checks if the passed value is an int.
            Raises a TypeError if it isn't."""
        if type(value) is not int:
            raise TypeError(f"{attribute_name} must be an integer")

    @staticmethod
    def dimensions_validator(dim_name, dim_value):
        """ Checks if the value for the dimension a positive number.
            Raises ValueError if it's not."""
        if dim_value < 1:
            raise ValueError(f"{dim_name} must be > 0")

    @staticmethod
    def coordinates_validator(coor_name, coor_value):
        """ Checks if the given value is not negative.
            Raises a ValueError id it is invalid."""
        if coor_value < 0:
            raise ValueError(f"{coor_name} must be >= 0")

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle.

            Args:
                value (int): The value to be set as the width of the
                            rectangle.
        """
        Rectangle.int_validator("width", value)
        Rectangle.dimensions_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

            Args:
                value (int): The value to be set as the height of the
                            rectangle.
        """
        Rectangle.int_validator("height", value)
        Rectangle.dimensions_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the value of the x cooridinate of the rectangle.

            Args:
                value (int): The value of the x cooridinate.
        """
        Rectangle.int_validator("x", value)
        Rectangle.coordinates_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for x attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the value of the y cooridinate of the rectangle.

            Args:
                value (int): The value of the y cooridinate.
        """
        Rectangle.int_validator("y", value)
        Rectangle.coordinates_validator("y", value)
        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle.

            Returns:
                int: the rectangle area.
        """
        return self.__height * self.__width

    def display(self):
        """ Prints a representaion of the rectangle using '#' character. """
        print(("\n" * self.__y) + self.__height * (
                (self.__x * " ") +
                (self.__width * "#") + "\n"), end="")

    def __str__(self):
        """ Genetrates a string representation of the rectangle instance
            containg the instance attributes values.

            Returns:
                str: string representaion of the instance.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Updates the attributes of a rectangle instance. Values can be
            passed either as positional arguments (args) or with their
            attribute names as keyword arguments (kwargs).

            Args:
                *args: Positional arguments representing values to be updated.
                        Must be in the order: "id", "width", "height", "x", "y"

                **kwargs: Keyword arguments representing attribute names and
                        their alues.
        """
        attributes = ["id", "width", "height", "x", "y"]
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
        """ Returns the dictionary representation of a Rectangle instance with
            the attributes: x, y, id, height, width.
        """
        attributes = ["x", "y", "id", "height", "width"]
        description = {}
        for attr in attributes:
            description[attr] = getattr(self, attr)
        return description
