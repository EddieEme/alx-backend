#!/usr/bin/env python3
"""A class LRUCache that inherits from BaseCaching and is a caching system."""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that implements an LRU caching system."""
    def __init__(self):
        """Initialize the LRUCache with an OrderedDict."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign item to self.cache_data with key following LRU rules."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = next(iter(self.cache_data))
                self.cache_data.pop(oldest_key)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Return the value in self.cache_data
        linked to key, updating LRU status."""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
