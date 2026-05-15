#!/usr/bin/env python3
"""Definition de la classe Rectangle qui herite de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defini par une largeur et une hauteur, valeurs validees."""

    def __init__(self, width, height):
        """Initialise un Rectangle avec width et height entiers positifs."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle (largeur multipliee par hauteur)."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne la description textuelle du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
