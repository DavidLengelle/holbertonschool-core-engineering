#!/usr/bin/env python3
"""Module that defines a VerboseList class extending the built-in list."""


class VerboseList(list):
    """List subclass that prints a message on every add or remove operation."""
    def append(self, item):
        """Append an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list with items and print a notification."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Print a notification and remove the first occurrence of item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and pop the item at the given index."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
