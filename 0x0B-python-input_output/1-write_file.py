#!/usr/bin/python3
"""Simple module."""


def write_file(filename="", text=""):
    """Write into a file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
