from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def send(self):
        pass


class Email(Observer):

    def send(self):
        pass


class Push(Observer):

    def send(self):
        pass


class SMS(Observer):

    def send(self):
        pass


class Observee(ABC):

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Reservation(Observee):
    _state: int = None
    _channels: List[Observer] = []

    def attach(self, channel: Observer):
        self._channels.append(channel)

    def detach(self, channel: Observer):
        self._channels.remove(channel)

    def notify(self):
        for channel in self._channels:
            channel.send()
