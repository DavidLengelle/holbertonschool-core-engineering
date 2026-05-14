#!/usr/bin/env python3
"""Module defining a Square class with size, position, area and printing"""


class Square:
    """Square class with size, position, area and string representation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size and a position"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validation"""

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def area(self):
        """Return the area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character"""

        print(self)

    def __str__(self):
        """Return the square as a printable string"""

        if self.size == 0:
            return ""

        lines = []
        for _ in range(self.position[1]):
            lines.append("")

        for _ in range(self.size):
            lines.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(lines)
