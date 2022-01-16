class Prop(object):
    def __init__(self):
        self.__start = None
        self.__end = None

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end
