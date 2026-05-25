#!/usr/bin/env python3
"""Read a text file and print it to stdout"""


def read_file(filename=""):
    """Read filename and print its content to standard output"""

    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
