#!/usr/bin/env python3
"""Print integers from a list."""


def print_list_integer(my_list=[]):
    """Print each integer of my_list on its own line."""
    
    for i in my_list:
        print("{:d}".format(i))
