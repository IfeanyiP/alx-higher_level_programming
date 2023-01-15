#!/usr/bin/python3
"""Defines a class mylist that inherits from list"""


class Mylist(list):
    """The class that inherits from list"""
    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
