from collections import Iterator, Iterable
from typing import List


class Amenity(object):
    def __init__(self, name, description, base_charge):
        self.name = name
        self.description = description
        self.base_charge = base_charge
        self.charge_per_hr = None

    def get_charge(self):
        pass


class Laundry(Amenity):
    def __init__(self, name, description, base_charge):
        super().__init__(name, description, base_charge)
        self.charge_per_hr = 20

    def get_charge(self, duration=0):
        return self.base_charge + duration * self.charge_per_hr


class RoomService(Amenity):
    def __init__(self, name, description, base_charge):
        super().__init__(name, description, base_charge)
        self.charge_per_hr = 20

    def get_charge(self, duration=0):
        return self.base_charge + duration * self.charge_per_hr


class KitchenService(Amenity):
    def __init__(self, name, description, base_charge):
        super().__init__(name, description, base_charge)
        self.charge_per_hr = 20

    def get_charge(self, duration=0):
        return self.base_charge + duration * self.charge_per_hr


class PoolService(Amenity):
    def __init__(self, name, description, base_charge):
        super().__init__(name, description, base_charge)
        self.charge_per_hr = 20

    def get_charge(self, duration=0):
        return self.base_charge + duration * self.charge_per_hr


class AmenityCollection(Iterable):
    def __init__(self, collection: List[Amenity]):
        self._collection = collection

    def __iter__(self):
        return AmenityIterator(self._collection)

    def add_item(self, item: Amenity):
        self._collection.append(item)

    def get_total_charge(self):
        cost = 0.0
        for amenity in self._collection:
            cost += amenity.get_charge()
        return cost


class AmenityIterator(Iterator):

    def __init__(self, collection: AmenityCollection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration()
        return value

    _position: int = None
