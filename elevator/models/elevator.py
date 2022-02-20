from queue import PriorityQueue

from elevator.models.enums.directions import Directions
from elevator.models.enums.locations import Locations
from elevator.models.request import Request


class Elevator(object):
    def __init__(self, current_floor):
        self.__curr_floor = current_floor
        self.direction = Directions.IDLE
        self._up_queue = PriorityQueue()
        self._down_queue = PriorityQueue()

    def send_up_request(self, request: Request):
        # request send up
        # first stop at the requester's floor
        if request.location == Locations.EXTERNAL:
            self._up_queue.put(Request(request.curr_floor, request.curr_floor, Directions.UP, Locations.EXTERNAL))
        self._up_queue.put(request)

    def send_down_request(self, request):
        if request.location == Locations.EXTERNAL:
            self._down_queue.put(
                Request(-1 * request.curr_floor, -1 * request.curr_floor, Directions.DOWN, Locations.EXTERNAL))
        request.curr_floor *= -1
        request.desired_floor *= -1
        self._down_queue.put(request)

    def run(self):
        while not self._up_queue.empty() or not self._down_queue.empty():
            self.process_requests()
        self.direction = Directions.IDLE

    def process_up_requests(self):
        while not self._up_queue.empty():
            request = self._up_queue.get()
            self.__curr_floor = request.desired_floor
        if not self._down_queue.empty():
            self.direction = Directions.DOWN
        else:
            self.direction = Directions.IDLE

    def process_down_requests(self):
        while not self._down_queue.empty():
            request = self._down_queue.get()
            self.__curr_floor = -1 * request.desired_floor
        if not self._down_queue.empty():
            self.direction = Directions.UP
        else:
            self.direction = Directions.IDLE

    def process_requests(self):
        if self.direction == Directions.UP or self.direction == Directions.IDLE:
            self.process_up_requests()
            self.process_down_requests()
        else:
            self.process_down_requests()
            self.process_up_requests()


if __name__ == '__main__':
    elevator = Elevator(0)
    req = Request
