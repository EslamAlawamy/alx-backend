#!/usr/bin/python3
""" LFU Caching module """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        super().__init__()
        self._lfu_keys = []

    def put(self, key, item):
        """ to add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self._lfu_keys.pop(self._lfu_keys.index(key))
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu = self._lfu_keys.pop(0)
                    del self.cache_data[lfu]
                    print(f"DISCARD: {lfu}")
                self.cache_data[key] = item
            self._lfu_keys.append(key)

    def get(self, key):
        """ to get an item by key """
        if key is not None and key in self.cache_data:
            self._lfu_keys.pop(self._lfu_keys.index(key))
            self._lfu_keys.append(key)
        return self.cache_data.get(key, None)
