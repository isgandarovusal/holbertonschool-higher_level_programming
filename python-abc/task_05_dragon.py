#!/usr/bin/env python3
"""
Module for mastering Mixins.
"""


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon using mixins."""

    def roar(self):
        """Print roaring action."""
        print("The dragon roars!")
