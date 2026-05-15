#!/usr/bin/env python3
"""Module defining the Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by a width and a height, both validated"""

    def __init__(self, width, height):
        """Initialize a Rectangle with positive integer width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
