#!/usr/bin/env python3
"""Module defining the Rectangle class with area and string representation"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by a width and a height, with area and str"""

    def __init__(self, width, height):
        """Initialize a Rectangle with positive integer width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle (width times height)"""

        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""

        return f"[Rectangle] {self.__width}/{self.__height}"
