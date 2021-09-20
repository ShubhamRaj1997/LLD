from abc import ABC, abstractmethod
from collections import OrderedDict


class LevelCache(object):
    def __init__(self, level, size, read_time, write_time, next_level=None, last_level=None, cache=None):
        self.read_time = read_time
        self.write_time = write_time
        self.size = size
        self.data = OrderedDict()
        self.level = level
        self.next_level = next_level
        self.last_level = last_level
        self._cache = cache

    @property
    def cache(self):
        if not self._cache:
            self._cache = LRUCacheStrategy(self.level, self.size)
        return self._cache

    @cache.setter
    def cache(self, cache):
        self._cache = cache

    def read(self, key):
        """

        :param key:
        :return: (read value, read time, write_time)
        """
        read_time = self.read_time
        write_time = 0.0
        val = self.cache.read(key)
        if val:
            return val, read_time, write_time
        elif self.next_level:
            val, next_read_time, next_write_time = self.next_level.read(key)
            read_time += next_read_time
            write_time += next_write_time
        if val:
            self.cache.write(key, val)
            write_time += self.write_time
        return val, read_time, write_time

    def write(self, key, val):
        """
        0 means not written since already written
        1 means written now
        :param key:
        :param val:
        :return:
        """
        write_time = self.read_time
        if self.cache.does_key_val_pair_exist(key, val):
            write_time += self.next_level.write(key, val) if self.next_level else 0.0
        else:
            self.cache.write(key, val)
            # read preference order in python
            write_time += self.write_time + (self.next_level.write(key, val) if self.next_level else 0.0)
        print(f"Write time was {write_time} , {self.write_time} for layer level {self.level}")
        return write_time


class CacheStrategy(ABC):
    def __init__(self, level=None, size=10):
        self.__data = OrderedDict()
        self.__level = level
        self.__size = size

    def __is_full(self):
        return len(self.__data.keys()) >= self.__size

    def does_key_val_pair_exist(self, key, val):
        return self.__data.get(key) == val

    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def write(self, key, val):
        pass


class LRUCacheStrategy(CacheStrategy):
    def __init__(self, level=None, size=10):
        super(LRUCacheStrategy, self).__init__(level=level, size=size)

    def write(self, key, val):
        if self.__is_full():
            """
            Can't write to this cache, Log here
            """
            popped_key, popped_val = self.__data.popitem(last=False)
            print(f"Cache level {self.__level} is Full, hence popped key {popped_key} and val {popped_val}")

        self.__data[key] = val
        self.__data.move_to_end(key)

    def read(self, key):
        if key not in self.__data:
            return None
        self.__data.move_to_end(key)
        return self.__data[key]

    # def __is_full(self):
    #     return len(self.__data.keys()) >= self.__size
    #
    # def does_key_val_pair_exist(self, key, val):
    #     return self.__data.get(key) == val

class LFUCacheStrategy(CacheStrategy):
    def __init__(self, level=None, size=10):
        super(LFUCacheStrategy, self).__init__(level=level, size=size)
        self.least_freq=1
        self.freq_list={}
        self.key_freq_map = {}

    def write(self, key, val):
        if self.__is_full():
            """
            Can't write to this cache, Log here
            """
            if self.least_freq not in self.freq_list:
                return
            popped_key = self.freq_list[self.least_freq][0]
            popped_val = self.__data.pop(popped_key)
            del self.freq_list[self.least_freq][0]
            print(f"Cache level {self.__level} is Full, hence popped key {popped_key} and val {popped_val}")
        self.__data[key] = val
        self.freq_list[1].appendleft(key)
        self.key_freq_map[key]=1
        self.least_freq = 1

    def read(self, key):
        if key not in self.__data:
            return None
        freq = self.key_freq_map[key]
        self.__data.move_to_end(key)
        return self.__data[key]


