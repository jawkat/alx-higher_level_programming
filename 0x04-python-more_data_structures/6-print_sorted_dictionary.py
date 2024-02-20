#!/usr/bin/python3
"""
     _summary_
    """


def print_sorted_dictionary(a_dictionary):
    """
    print_sorted_dictionary _summary_

    Args:
        a_dictionary (_type_): _description_
    """
    for key,value in sorted(a_dictionary.items()):
        print (f"{key}: {value}")
