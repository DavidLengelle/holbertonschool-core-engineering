#!/usr/bin/env python3
"""Add two tuples and return a tuple with exactly two integers."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return (t_a[0]+t_b[0], t_a[1]+t_b[1]); missing values count as 0."""

    t_a = tuple_a + (0, 0)
    t_b = tuple_b + (0, 0)
    return (t_a[0] + t_b[0], t_a[1] + t_b[1] )
