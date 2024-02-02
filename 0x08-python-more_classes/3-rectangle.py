#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle. No body."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calcul area of rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Calcul permiter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2*(self.__height + self.__width))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))