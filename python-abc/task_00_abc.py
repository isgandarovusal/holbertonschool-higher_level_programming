#!/usr/bin/env python3
"""
Module for Abstract Animal Class and its Subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to define the sound of the animal."""
        pass


class Dog(Animal):
    """Class representing a Dog."""

    def sound(self):
        """Return the sound of a Dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat."""

    def sound(self):
        """Return the sound of a Cat."""
        return "Meow"
