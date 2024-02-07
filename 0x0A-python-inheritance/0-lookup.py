#!/usr/bin/python3
"""Simple lockup module."""


def lookup(obj):
    """
        The lookup func

        Parameters:
            obj: The obj to be printed.
        """
    return list(dir(obj))
