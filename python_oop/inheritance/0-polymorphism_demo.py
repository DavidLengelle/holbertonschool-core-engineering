#!/usr/bin/env python3
"""Demonstration de l'heritage et du polymorphisme avec des animaux."""


class Animal:
    """Classe parent representant un animal generique."""

    def speak(self):
        """Retourne le son par defaut d'un animal."""
        return "Some sound"


class Dog(Animal):
    """Sous-classe d'Animal representant un chien."""

    def speak(self):
        """Retourne le son emis par un chien."""
        return "Woof"


class Cat(Animal):
    """Sous-classe d'Animal representant un chat."""

    def speak(self):
        """Retourne le son emis par un chat."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
