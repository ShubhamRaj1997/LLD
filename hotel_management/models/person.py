import itertools


class Person(object):
    def __init__(self, name, address, email, phone, account_type):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.account_type = account_type
        self.account = Account


class Account(object):
    itr = itertools.count

    def __init__(self, password, status, _id=None):
        self._id = _id or next(self.itr)
        self.password = password
        self.status = status

    def reset_password(self):
        pass


class HouseKeeper(Person):
    def __init__(self, name, address, email, phone, account_type):
        super().__init__(name, address, email, phone, account_type)

    def assign_to_room(self):
        pass


class Receptionist(Person):
    def __init__(self, name, address, email, phone, account_type):
        super().__init__(name, address, email, phone, account_type)

    def create_booking(self, person_id, checkin, checkout, room):
        pass


class Guest(Person):
    def __init__(self, name, address, email, phone, account_type):
        super().__init__(name, address, email, phone, account_type)

    def create_booking(self, checkin, checkout, room):
        pass


class Server(Person):
    def __init__(self, name, address, email, phone, account_type):
        super().__init__(name, address, email, phone, account_type)

    def add_room_charge(self, charge, room):
        pass
