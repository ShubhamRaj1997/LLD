class LevelCacheData(object):
    def __init__(self, read_time, write_time, size=10):
        self.__write_time = write_time
        self.__read_time = read_time
        self.__size = size

    @property
    def write_time(self):
        return self.__write_time

    @write_time.setter
    def write_time(self, write_time):
        self.__write_time = write_time

    @property
    def read_time(self):
        return self.__read_time

    @read_time.setter
    def read_time(self, read_time):
        self.__read_time = read_time

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size




