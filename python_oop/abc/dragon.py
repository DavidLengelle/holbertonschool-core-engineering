#!/usr/bin/env python3
"""Module that demonstrates mixins with a Dragon class."""


class SwimMixin:
    """Mixin that provides swimming behavior."""
    def swim(self):
        """Print a message about the creature swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""
    def fly(self):
        """Print a message about the creature flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class that combines SwimMixin and FlyMixin to represent a dragon."""
    def roar(self):
        """Print a message about the dragon roaring."""
        print("The dragon roars!")
