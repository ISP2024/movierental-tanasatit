import logging
from pricing import *


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    # # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, movie, days_rented, price_code):
        """
        Initialize a new movie rental object for a movie
        with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code
        self.set_price_code(price_code)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def set_price_code(self, price_code):
        if price_code == self.REGULAR:
            self.price_code = RegularPrice()
        elif price_code == self.NEW_RELEASE:
            self.price_code = NewRelease()
        elif price_code == self.CHILDREN:
            self.price_code = ChildrensPrice()
        else:
            log = logging.getLogger()
            log.error(f"Movie {self.title} has unrecognized priceCode {price_code}")
            raise ValueError("Invalid price code")

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self) -> float:
        return self.movie.price_code.get_price(self.days_rented)

    def get_rental_points(self) -> int:
        return self.movie.price_code.get_rental_points(self.days_rented)
