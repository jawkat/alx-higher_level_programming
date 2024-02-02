#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle with width, height, area, and perimeter."""

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.width = width
        self.height = height

    @prop
    erty
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with error checking."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with error checking."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":
    # Test the implementation with the provided main program
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # Create a new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
