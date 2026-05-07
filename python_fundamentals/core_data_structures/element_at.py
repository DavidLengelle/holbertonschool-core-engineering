#!/usr/bin/env python3
"""Safely retrieve an element from a list by index (C-style bounds)."""


def element_at(my_list, idx):
    """Return my_list[idx] or None if idx is negative or out of range."""

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
