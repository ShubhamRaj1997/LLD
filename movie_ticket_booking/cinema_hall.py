class CinemaHall(object):
    def __init__(self, name, total_seats, seats, shows, current_show):
        self.current_show = current_show
        self.shows = shows
        self.seats = seats
        self.total_seats = total_seats
        self.name = name


