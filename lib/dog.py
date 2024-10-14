#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        """Initializes a Dog instance with a name and breed.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog. Defaults to "Mutt".
        """
        self.name = name
        self.breed = breed

    def bark(self):
        """Makes the dog bark."""
        print("Woof!")

    def sit(self):
        """Makes the dog sit."""
        print("The dog is sitting.")