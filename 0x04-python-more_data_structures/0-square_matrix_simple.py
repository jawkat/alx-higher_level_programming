#!/usr/bin/python3
"""_summary_"""


def square_matrix_simple(matrix=[]):
    """_summary_

    Args:
        matrix (list, optional): _description_. Defaults to [].
    """
    return [[num**2 for num in row] for row in matrix]
