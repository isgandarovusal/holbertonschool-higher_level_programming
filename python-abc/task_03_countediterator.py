#!/usr/bin/env python3
"""
Module for CountedIterator - Keeping Track of Iteration.
"""


class CountedIterator:
    """A custom iterator that keeps track of the number of items iterated."""

    def __init__(self, some_iterable):
        """Initialize the iterator and the counter."""
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.count

    def __next__(self):
        """Fetch the next item from the original iterator and increment count."""
        item = next(self.iterator)
        self.count += 1
        return item
