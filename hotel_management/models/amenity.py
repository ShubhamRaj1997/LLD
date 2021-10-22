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


