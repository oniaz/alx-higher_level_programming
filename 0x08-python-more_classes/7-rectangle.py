#!/usr/bin/python3
"""A module representing a rectangle """


class Rectangle:
    """A class representing a rectangle

        Attributes:
            number_of_instances (int): counts the current number of instances.
            print_symbol (string): symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with given width and height
        and increments Rectangle.number_of_instances.

        Args:
            size (width): The width of the rectangle.
            size (height): The height of the rectangle.

        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the rectangle.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
        - value (int): The value to be set as the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
        - value (int): The value to be set as the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width and self.__height:
            return (self.__width * 2) + (self.__height * 2)
        return 0

    def __str__(self):
        """Returns a string representation of the rectangle using
        self.print_symbol. If the width or the height is equal to 0, it
        returns an empty string.

        Returns:
            string: A representation of the rectangle using '#' or empty
            string if the width or the height is equal to zero.
        """
        if self.__width and self.__height:
            return (str(self.print_symbol) * self.__width + "\n") *\
                (self.__height - 1) + str(self.print_symbol) * self.__width
        return ""

    def __repr__(self):
        """Return a string representation of the rectangle to be able to
        recreate a new instance by using eval().

        Returns:
        string: a string representation of the rectangle.
        """
        return "Rectangle(" + str(self.__width) + ", " + \
            str(self.__height) + ")"

    def __del__(self):
        """Prints the message "Bye rectangle..." when an instance of
        Rectangle is deleted and decrements Rectangle.number_of_instances.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
