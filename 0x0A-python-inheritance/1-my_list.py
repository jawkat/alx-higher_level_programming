#!/usr/bin/python3
""" print sorted list """

class MyList(list):
    """ My User list """

    def __init__(self):
        """constructor method"""
        super().__init__()

    def print_sorted(self):
        """print the list
        """
        print(sorted(self))
