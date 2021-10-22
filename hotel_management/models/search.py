from abc import ABC, abstractmethod


class Search(ABC):
    @staticmethod
    @abstractmethod
    def search_rooms(checkin_date, checkout_date, location:str):
        return []
