#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance with a FlyingFish class."""


class Fish:
    """Class that represents a fish."""
    def swim(self):
        """Print a message about the fish swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message about the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Class that represents a bird."""
    def fly(self):
        """Print a message about the bird flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message about the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class that inherits from both Fish and Bird."""
    def swim(self):
        """Print a message about the flying fish swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print a message about the flying fish soaring."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print a message about the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
