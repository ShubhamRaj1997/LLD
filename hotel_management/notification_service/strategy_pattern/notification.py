from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def send(self):
        pass


class Email(Channel):

    def send(self):
        pass


class Push(Channel):

    def send(self):
        pass


class SMS(Channel):

    def send(self):
        pass


class Notification(object):
    def __init__(self, channel: Channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel


class SendNotification(Notification):
    def __init__(self, channel):
        super(SendNotification, self).__init__(channel)

    def send(self):
        self._channel.send()
