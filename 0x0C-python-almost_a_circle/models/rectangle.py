#!/usr/bin/python3
""" Module representing a Rectangle """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class. A subclass of Base class. """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ initializing the rectangle instance.

            Args:
                width (int): the width of the rectangle.
                height (int): the height of the rectangle.
                x (int):
                y (int):
                id (int): the instance id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def int_validator(attribute_name, value):
        """ Checks if the passed value is an int.
            Raises a TypeError if it isn't."""
        if type(value) is not int:
            raise TypeError(f"{attribute_name} must be an integer")

    def dimensions_validator(dim_name, dim_value):
        """ Checks if the value for the dimension a positive number.
            Raises ValueError if it's not."""
        if dim_value < 1:
            raise ValueError(f"{dim_name} must be > 0")

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
        """ Sets the x value of the rectangle.

            Args:
                value (int): The value of x.
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
        """ Sets the y of the rectangle.

            Args:
                value (int): The value of y.
        """
        Rectangle.int_validator("y", value)
        Rectangle.coordinates_validator("y", value)
        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.__height * self.__width

    def display(self):
        """ prints a representaion of the rectangle using '#' character. """
        print(("\n" * self.__y) + self.__height * (
                (self.__x * " ") +
                (self.__width * "#") + "\n"), end="")

    def __str__(self):
        """ Returns a string with the rectangle attributes values. """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Updates the attributes of an object. Values can be passed either as
            positional arguments (args) or with their attribute names as
            keyword arguments (kwargs).

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
