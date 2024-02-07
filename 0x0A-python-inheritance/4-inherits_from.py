#!/usr/bin/python3
"""Simple class module."""


def inherits_from(obj, a_class):
    """
    Check if the obj is an instance of the specified class

    Parameters:
        obj: the obj to check.
        a_class: the class itself
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
