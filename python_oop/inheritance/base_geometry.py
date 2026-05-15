#!/usr/bin/env python3
"""Module defining the BaseGeometry class"""


class BaseGeometry:
    """Base class representing a generic geometric shape"""

    def area(self):
        """Raise an exception because the method is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly positive integer"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
