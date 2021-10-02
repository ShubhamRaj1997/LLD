import itertools

# city should have only state and zip codes, address should be of a cinema hall not the city
class City(object):
    itr = itertools.count()

    def __init__(self, name, zip_code, state):
        self._id = next(self.itr)
        self.name = name
        self.zip_code = zip_code
        self.state = state
        self.cinemas = []

    def add_cinema(self, cinema):
        if cinema not in self.cinemas:
            self.cinemas.append(cinema)

    def remove_cinema(self, cinema):
        self.cinemas.remove(cinema)
