#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that represents an animal."""
    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """Subclass of Animal that represents a dog."""
    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal that represents a cat."""
    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"
