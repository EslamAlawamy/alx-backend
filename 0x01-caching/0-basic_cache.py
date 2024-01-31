#!/usr/bin/python3
""" Basic dictionary module """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        """ to add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ to get an item by a key """
        return self.cache_data.get(key, None)
