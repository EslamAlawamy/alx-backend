#!/usr/bin/python3
""" MRU Caching module """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        super().__init__()
        self._mru_keys = []

    def put(self, key, item):
        """ to add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self._mru_keys:
                self._mru_keys.remove(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                removed_key = self._mru_keys.pop()
                del self.cache_data[removed_key]
                print(f"DISCARD: {removed_key}")
            self._mru_keys.append(key)

    def get(self, key):
        """ to get an item by key """
        if key in self.cache_data.keys():
            self._mru_keys.pop(self._mru_keys.index(key))
            self._mru_keys.append(key)
        return self.cache_data.get(key, None)
