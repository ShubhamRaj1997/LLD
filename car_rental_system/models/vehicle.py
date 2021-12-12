from car_rental_system.enums.vehicle_type import VehicleType, VehicleStatus
from car_rental_system.models.reservation import Reservation


class Vehicle(object):
    def __init__(self, liscence_no: str, passenger_capacity: int, vehicle_type: VehicleType,
                 vehicle_status: VehicleStatus):
        self.vehicle_status = vehicle_status
        self.vehicle_type = vehicle_type
        self.passenger_capacity = passenger_capacity
        self.liscence_no = liscence_no


