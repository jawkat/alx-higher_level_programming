#!/usr/bin/python3
""" Module matrix division """


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.

    Args:
        matrix: the matrix of element
        div: element that divides

    Raises:
        TypeError: matrix must be a list of lists of integers or floats
        TypeError: Each row of the matrix must be of the same size
        TypeError: div must be a number (integer or float)
        ZeroDivisionError: div can’t be equal to 0

    Returns: a new matrix representing the result of the division

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must be of the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a list of lists of " +
                                "integers or floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/2-matrix_divided.txt")
