#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements a simple caching system
    """

    def put(self, key, item):
        """ Add an item to the cache
        Args:
            key: Key to identify the item
            item: Value to be stored in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache
        Args:
            key: Key to identify the item
        Returns:
            Value associated with the key in the cache, or None if not found
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
