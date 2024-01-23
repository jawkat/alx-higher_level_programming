#!/usr/bin/python3

"""Square and set size as private instance variable"""


class Square:
    """The class to create square."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size (int): the size of the square

        Raises:
            TypeError : if size is an integer
            ValueError: if size < 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """ Area of this square.
            Returns :
                the size squared.
            """
            return self.__size ** 2
