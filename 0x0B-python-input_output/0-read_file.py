#!/usr/bin/python3
"""Simple module."""


def read_file(filename=""):
    """Read a file into stdout."""
    with open(filename, "r") as f:
        print(f.read())
