from abc import ABC, abstractmethod
from typing import List

from car_rental_system.enums.vehicle_type import VehicleType
from car_rental_system.models.vehicle import Vehicle


class Search(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def search_by_type(self, vehicle_type: VehicleType) -> List[Vehicle]:
        pass

    @abstractmethod
    def search_by_model(self, model_name: str) -> List[Vehicle]:
        pass


class VehicleInventory(Search):
    def search_by_type(self, query):
        return self.__vehicle_types.get(query)

    def search_by_model(self, query):
        return self.__vehicle_models.get(query)

    def __init__(self):
        super().__init__()
        self.__vehicle_types = {}
        self.__vehicle_models = {}
