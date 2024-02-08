#!/usr/bin/python3
"""chech if the object is instance of a class
"""

def is_kind_of_class(obj, a_class):
    """check if a object is a kind of class

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        boolein : true if obj is a kind of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
