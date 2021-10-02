class Movie(object):
    def __init__(self, title, description, genre, duration, language, certificate, release_date, country):
        self.country = country
        self.release_date = release_date
        self.certificate = certificate
        self.language = language
        self.duration = duration
        self.genre = genre
        self.description = description
        self.title = title
        self.__shows = []

    @property
    def shows(self):
        return self.__shows

    def add_show(self, show):
        self.shows.append(show)

    def remove_show(self, show):
        self.shows.remove(show)


class MovieService(object):
    def __init__(self):
        pass

    def fetch_movies(self, query):
        # do database query for movie
        # db.Movies.find(query)
        return []
