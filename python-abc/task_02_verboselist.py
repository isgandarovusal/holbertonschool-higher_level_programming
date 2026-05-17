#!/usr/bin/env python3
"""
Module for Extending the Python List with Notifications.
"""


class VerboseList(list):
    """A custom list class that prints notifications upon modification."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove an item and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
