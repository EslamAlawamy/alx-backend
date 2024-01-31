#!/usr/bin/python3
""" FIFO caching module """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def put(self, key, item):
        """ to add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = sorted(self.cache_data.keys())[0]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ to get an item by key """
        return self.cache_data.get(key, None)
