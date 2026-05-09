#!/usr/bin/env python3
"""Find the key with the highest integer value in a dictionary."""


def best_score(a_dictionary):
    """Return the key with the biggest value, or None if dict is None/empty."""

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = list(a_dictionary.keys())[0]

    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[best_key]:
            best_key = key

    return best_key
