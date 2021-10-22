from abc import ABC, abstractmethod


# use this only when we have limited number of caches,
# it is good code but again will get change and added whenever a new cache Level is added
class CacheHandler(ABC):
    @abstractmethod
    def set_next(self, cache_handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractCacheHandler(CacheHandler):
    _next_handler: CacheHandler = None

    def set_next(self, cache_handler):
        self._next_handler = cache_handler
        return cache_handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class L1CacheHandler(AbstractCacheHandler):
    def handle(self, request):
        # check if value is present handle it
        # else
        return super().handle(request)


class L2CacheHandler(AbstractCacheHandler):
    def handle(self, request):
        # check if value is present handle it
        # else
        return super().handle(request)


class L3CacheHandler(AbstractCacheHandler):
    def handle(self, request):
        # check if value is present handle it
        # else
        return super().handle(request)


if __name__ == "__main__":
    l1 = L1CacheHandler()
    l2 = L2CacheHandler()
    l3 = L3CacheHandler()
    l1.set_next(l2).set_next(l3)
    # start reading cache from L1
