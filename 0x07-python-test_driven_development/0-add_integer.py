#!/usr/bin/python3
""" Module for add_integer method."""


def add_integer(a, b=98):
    """
    function that adds 2 integers.

    Args:
        a: int or float
        b: int or float (default as 98)

    Raises:
        TypeErrors: if a or b is not an int or float

        Returns:
        int: the addition of a and b
    """

    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integers.txt")
