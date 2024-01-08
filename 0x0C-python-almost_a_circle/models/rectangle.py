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

    def int_validator(name, n):
        if type(n) is not int:
            raise TypeError(f"{name} must be an integer")

    def dimensions_validator(name, dim):
        if dim < 1:
            raise ValueError(f"{name} must be > 0")

    def coordinates_validator(name, coor):
        if coor < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """ getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
        - value (int): The value to be set as the width of the rectangle.
        """
        Rectangle.int_validator("width", value)
        Rectangle.dimensions_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
        - value (int): The value to be set as the height of the rectangle.
        """
        Rectangle.int_validator("height", value)
        Rectangle.dimensions_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x of the rectangle.

        Args:
        - value (int): The value of x.
        """
        Rectangle.int_validator("x", value)
        Rectangle.coordinates_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter for x attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y of the rectangle.

        Args:
        - value (int): The value of y.
        """
        Rectangle.int_validator("y", value)
        Rectangle.coordinates_validator("y", value)
        self.__y = value

    def area(self):
        """ calculates the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        # for h in range(self.__height):
        #     for w in range(self.__width):
        print(("\n" * self.__y) + self.__height * ((self.__x * " ") + (self.__width * "#") + "\n"), end="")

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            try:
                for i in range(len(args)):
                    setattr(self, attributes[i], args[i])
            except(IndexError):
                pass
        else:
                for key, value in kwargs.items():
                    if key in attributes:
                        setattr(self, key, value)

