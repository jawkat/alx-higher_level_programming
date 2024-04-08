#!/usr/bin/python3
"""
     _summary_

"""


def search_replace(my_list, search, replace):
    """
    search_replace _summary_

    Args:
        my_list (_type_): _description_
        search (_type_): _description_
        replace (_type_): _description_
    """
    new_list = []
    for i, item in enumerate(my_list):
        if item != search:
            new_list.append(item)
        else:
            new_list.append(replace)
    return new_list
