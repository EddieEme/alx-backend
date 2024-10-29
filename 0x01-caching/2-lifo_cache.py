#!/usr/bin/env python3
"""A class LIFOCache that inherits from BaseCaching and is a caching system.

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded followed by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that implements a LIFO caching system."""
    def __init__(self):
        """Initialize the LIFOCache with an empty order list."""
        super().__init__()
        self.order = []  # Keeps track of the order of insertion for LIFO

    def put(self, key, item):
        """Assign item to self.cache_data with key following LIFO rules."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
