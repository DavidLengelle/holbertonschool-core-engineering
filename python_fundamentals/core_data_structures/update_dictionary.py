#!/usr/bin/env python3
"""Update or add a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace value if key exists, otherwise create it; return the dict."""

    a_dictionary[key] = value
    return a_dictionary
