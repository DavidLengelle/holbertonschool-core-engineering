#!/usr/bin/env python3
"""Module that safely prints the first x elements of a list"""


def safe_print_list(my_list=[], x=0):
    """Print at most x elements of my_list on a single line"""
    count = 0

    for i in range(x):

        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break

    print()
    return count
