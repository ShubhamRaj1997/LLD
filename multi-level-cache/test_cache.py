from level_cache import *
from level_cache_data import LevelCacheData


class TestCache(object):
    def __init__(self, levels, last_x):
        self.last_x = last_x
        self.levels = levels

    def run(self):
        level_caches = [
            LevelCache(1, 10, LevelCacheData(1, 1, 10), cache=LRUCacheStrategy()),
            LevelCache(2, 10, LevelCacheData(1, 1, 10), cache=LRUCacheStrategy()),
            LevelCache(1, 10, LevelCacheData(1, 1, 10), cache=LRUCacheStrategy()),
            LevelCache(1, 10, LevelCacheData(1, 1, 10), cache=LFUCacheStrategy()),
            LevelCache(1, 10, LevelCacheData(1, 1, 10), cache=LRUCacheStrategy()),
            LevelCache(1, 10, LevelCacheData(1, 1, 10), cache=LRUCacheStrategy()),
            LastLevelCache()

        ]
        for level in range(0, len(level_caches) - 1):
            level_caches[level].next_level = level_caches[level + 1]
        # run tests here asw well