#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited
"""
def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: true if the object is an instance of a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
