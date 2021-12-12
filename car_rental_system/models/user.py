class User(object):
    def __init__(self, user_id: str, name: str):
        self.name = name
        self.user_id = user_id
        self._reserved_vehicles = []

