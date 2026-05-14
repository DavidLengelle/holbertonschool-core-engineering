#!/usr/bin/env python3
"""Module defining a Square class with size, area and printing"""


class Square:
    """Square class with size, area and a my_print method"""

    def __init__(self, size=0):
        """Initialize the square by assigning size through the setter"""

        self.size = size

    @property
    def size(self):
        """Get the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character"""

        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            print("#" * self.size)
