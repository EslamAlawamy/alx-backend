#!/usr/bin/python3
""" LRU Caching module """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        super().__init__()
        self._lru_keys = []

    def put(self, key, item):
        """ to add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self._lru_keys:
                self._lru_keys.remove(key)
            self._lru_keys.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                removed_key = self._lru_keys.pop(0)
                del self.cache_data[removed_key]
                print(f"DISCARD: {removed_key}")

    def get(self, key):
        """ to get an item by key """
        if key in self.cache_data.keys():
            self._lru_keys.pop(self._lru_keys.index(key))
            self._lru_keys.append(key)
        return self.cache_data.get(key, None)
