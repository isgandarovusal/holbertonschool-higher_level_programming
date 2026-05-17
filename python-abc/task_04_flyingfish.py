#!/usr/bin/env python3
"""
Module for exploring multiple inheritance with a FlyingFish.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a FlyingFish, inheriting from Fish and Bird."""

    def fly(self):
        """Print flying behavior of FlyingFish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior of FlyingFish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat of FlyingFish."""
        print("The flying fish lives both in water and the sky!")
