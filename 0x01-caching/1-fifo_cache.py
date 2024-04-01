#!/usr/bin/env python3
""" FIFO Cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implements FIFO caching strategy
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache using FIFO strategy
        Args:
            key: Key to identify the item
            item: Value to be stored in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.queue.append(key)
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
