#!/usr/bin/python3
"""Simple class module."""


def is_same_class(obj, a_class):
    """
    Check if the obj is an instance of the specified class

    Parameters:
        obj: the obj to check.
        a_class: the class itself
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
