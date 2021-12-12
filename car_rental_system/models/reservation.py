import datetime

from car_rental_system.enums.reservation_status import ReservationStatus
from car_rental_system.enums.vehicle_type import VehicleStatus
from car_rental_system.models.vehicle import Vehicle


class Reservation(object):
    def __init__(self, reservation_number: int, vehicle:Vehicle):
        self.__reservation_number = reservation_number
        self.__creation_date = datetime.datetime.now()
        self.__status = ReservationStatus.INITIATED
        self.__due_date = datetime.datetime.now()
        self.__vehicle = vehicle

    @property
    def vehicle(self):
        return self.__vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        self.__vehicle = vehicle

    def fetch_details(self):
        return vars(self)

    def reserve(self):
        self.vehicle.vehicle_status=VehicleStatus.RESERVED

    def unreserve(self):
        self.vehicle.vehicle_status=VehicleStatus.AVAILABLE
