#!/usr/bin/env python3
"""Write a string to a text file"""


def write_file(filename="", text=""):
    """Write text to filename and return the number of characters written"""

    with open(filename, mode="w", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
