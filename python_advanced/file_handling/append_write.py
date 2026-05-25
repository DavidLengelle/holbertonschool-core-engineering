#!/usr/bin/env python3
"""Append a string at the end of a text file"""


def append_write(filename="", text=""):
    """Append text to filename and return the number of characters added"""

    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
