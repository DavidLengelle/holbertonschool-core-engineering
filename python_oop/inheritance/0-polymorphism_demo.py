#!/usr/bin/env python3
"""Module demonstrating inheritance and polymorphism with animals"""


class Animal:
    """Parent class representing a generic animal"""

    def speak(self):
        """Return the default sound of an animal"""

        return "Some sound"


class Dog(Animal):
    """Subclass of Animal representing a dog"""

    def speak(self):
        """Return the sound made by a dog"""

        return "Woof"


class Cat(Animal):
    """Subclass of Animal representing a cat"""

    def speak(self):
        """Return the sound made by a cat"""

        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
