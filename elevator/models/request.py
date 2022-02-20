class Request(object):
    def __init__(self, curr_floor, desired_floor, direction, location):
        self.curr_floor = curr_floor
        self.desired_floor = desired_floor
        self.direction = direction
        self.location = location
        c