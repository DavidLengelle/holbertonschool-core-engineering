#!/usr/bin/env python3
"""print a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    """Print each row of matrix; values separated by a single space."""

    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d}".format(row[i]), end=" ")
    print()
    