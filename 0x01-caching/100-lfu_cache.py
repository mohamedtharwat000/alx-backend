#!/usr/bin/env python3
""" LFU Cache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements LFU caching strategy
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item to the cache using LFU strategy
        Args:
            key: Key to identify the item
            item: Value to be stored in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                else:
                    min_freq_key = min(self.frequency[self.min_frequency])
                    del self.cache_data[min_freq_key]
                    del self.frequency[self.min_frequency][min_freq_key]
                print("DISCARD:", min_freq_key)
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            if self.frequency[key] == 1:
                self.min_frequency = 1
            else:
                self.min_frequency = min(self.frequency.values())

    def get(self, key):
        """ Retrieve an item from the cache
        Args:
            key: Key to identify the item
        Returns:
            Value associated with the key in the cache, or None if not found
        """
        if key is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                if self.frequency[key] == 1:
                    self.min_frequency = 1
                else:
                    self.min_frequency = min(self.frequency.values())
                return self.cache_data[key]
        return None
