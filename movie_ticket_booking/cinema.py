from movie_ticket_booking.location import Location


class Cinema(object):
    def __init__(self, location: Location):
        self.location = location
        self.cinema_halls = []
