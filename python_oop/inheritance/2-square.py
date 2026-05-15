#!/usr/bin/env python3
"""Module defining the Square class that inherits from Rectangle"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a size, a specialized Rectangle"""

    def __init__(self, size):
        """Initialize a Square with a positive integer size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square"""

        return f"[Square] {self.__size}/{self.__size}"
