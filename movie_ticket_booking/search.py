from abc import ABC

from movie_ticket_booking.movie import MovieService


class Search(ABC):
    def search_by_title(self, title):
        pass

    def search_by_lang(self, language):
        pass

    def search_by_genre(self, genre):
        pass

    def search_by_city(self, city_name):
        pass


class MovieSearch(Search):
    def __init__(self):
        self.movie_service = MovieService()

    def search_by_title(self, title):
        return self.movie_service.fetch_movies({"title": title})

    def search_by_genre(self, genre):
        return self.movie_service.fetch_movies({"genre": genre})

    def search_by_lang(self, language):
        return self.movie_service.fetch_movies({"language": language})

    def search_by_city(self, city_name):
        return self.movie_service.fetch_movies({"cities": city_name})
    
