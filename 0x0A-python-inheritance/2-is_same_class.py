#!/usr/bin/python3
"""
    verifie is the object is an instance of a class
"""


def is_same_class(obj, a_class):
    """function returns True if the object is the same class

    Args:
        obj (object): obejct
        a_class (class): class to check

    Returns: true if the object is the same class
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
