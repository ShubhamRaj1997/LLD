import statistics

from singleton import Singleton


class Stats(metaclass=Singleton):
    def __init__(self, last_x):
        self.read_times = []
        self.write_times = []
        self.last_x = last_x

    def get_last_read_times(self, last):
        return statistics.mean(self.read_times[-1*last:])

    def get_last_write_times(self, last):
        return statistics.mean(self.write_times[-1*last:])

    def record_read(self, t):
        if len(self.read_times) == self.last_x:
            del self.read_times[0]
        self.read_times.append(t)

    def record_write(self, t):
        if len(self.write_times) == self.last_x:
            del self.write_times[0]
        self.write_times.append(t)
