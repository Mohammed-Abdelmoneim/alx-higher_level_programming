#!/usr/bin/python3
"""Simple module."""


def append_write(filename="", text=""):
    """Append to a file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
