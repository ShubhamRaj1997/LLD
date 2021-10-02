from movie_ticket_booking.movie import Movie


class CinemaShow(object):
    def __init__(self, start_time, end_time, movie: Movie):
        self.movie = movie
        self.end_time = end_time
        self.start_time = start_time
