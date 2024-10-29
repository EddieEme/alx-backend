#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching
and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that implements an MRU caching system."""

    def __init__(self):
        """Initialize the MRUCache with an OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign item to self.cache_data with key following MRU rules."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recent_key = next(reversed(self.cache_data))
                self.cache_data.pop(most_recent_key)
                print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """Return the value in self.cache_data
        linked to key, updating MRU status."""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
