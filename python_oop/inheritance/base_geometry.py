#!/usr/bin/env python3
"""Definition de la classe de base BaseGeometry."""


class BaseGeometry:
    """Classe de base representant une forme geometrique generique."""

    def area(self):
        """Leve une exception car la methode n'est pas encore implementee."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier strictement positif."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
