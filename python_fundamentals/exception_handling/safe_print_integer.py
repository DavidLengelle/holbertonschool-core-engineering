#!/usr/bin/env python3
"""Module that safely prints a value as an integer"""


def safe_print_integer(value):
    """Print value formatted as an integer"""
    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError):
        return False
