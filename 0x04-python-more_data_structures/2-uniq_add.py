#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    uniq_add _summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    res = 0
    new_list = set(my_list)
    for i, item in enumerate(new_list):
        res += item

    return res
