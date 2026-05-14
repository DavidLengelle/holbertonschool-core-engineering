#!/usr/bin/env python3
"""Module that defines a Square class with size validation and an area method"""


class Square:
    """Square class with a validated private size and an area method"""

    def __init__(self, size=0):
        """Initialize the square after validating size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size
