#!/usr/bin/env python3
"""Module that reads a text file and prints it to standard output."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
