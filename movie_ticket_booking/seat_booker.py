class SeatBooker(object):
    def __init__(self):
        self.__booked_seats = {}

    def book_seats(self, show, seats):
        self.__booked_seats[show].extend(seats)

    def is_seat_book(self, show, seat):
        return seat in self.__booked_seats[show]

    def unbook_seat(self, show, seat):
        self.__booked_seats[show].pop(seat)

