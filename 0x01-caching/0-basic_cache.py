#!/usr/bin/env python3
"""A class BasicCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from
    BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """Assign item to self.cache_data with key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self.cache_data."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
