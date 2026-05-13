#!/usr/bin/env python3
"""Module that safely divides two numbers"""


def safe_print_division(a, b):
    """Divide a by b and print the result, returning it or None on failure"""

    try:
        result = a / b

    except (ZeroDivisionError, TypeError):
        result = None

    finally:
        print("Inside result: {}".format(result))

    return result
