#!/usr/bin/env python3
"""Module that writes a string to a text file and counts the characters."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the characters written.

    The file is created if it does not exist and overwritten otherwise.

    Args:
        filename (str): The path of the file to write to.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        nb = f.write(text)
    return nb
