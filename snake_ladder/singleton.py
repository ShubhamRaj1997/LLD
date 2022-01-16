"""
type vs object
Remember: singleton is anti pattern, if you want to write singleton in better way , better is to make it thread safe
"""
import threading


class SingletonMeta(type):
    _instances = dict()
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
