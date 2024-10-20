import logging
from pricing import PriceCode, NewRelease, ChildrensPrice, RegularPrice  # Adjust imports as needed
import pandas as pd
from movie import Movie

log = logging.getLogger(__name__)

class Rental:
    """
    A rental of a movie by a customer.
    This class holds the movie, rental period, and price information.
    """

    def __init__(self, movie: Movie, days: int):
        """
        Initialize a new movie rental object for a movie
        with a known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days
        self.price_code = self.price_code_for_movie(movie)  # Automatically set price code based on the movie

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def price_code_for_movie(self, movie: Movie):
        """Determine the price code for a movie."""
        current_year = pd.Timestamp.now().year
        if movie.year == current_year:
            return PriceCode.NEW_RELEASE
        elif any(genre.lower() in ["children", "childrens"] for genre in movie.genre):
            return PriceCode.CHILDREN
        else:
            return PriceCode.REGULAR

    def get_price_code(self):
        # Get the price code
        return self.price_code

    def get_price(self) -> float:
        """Calculate the price of the rental based on the price code."""
        if self.price_code == PriceCode.REGULAR:
            return RegularPrice().get_price(self.days_rented)
        elif self.price_code == PriceCode.NEW_RELEASE:
            return NewRelease().get_price(self.days_rented)
        elif self.price_code == PriceCode.CHILDREN:
            return ChildrensPrice().get_price(self.days_rented)

    def get_rental_points(self) -> int:
        """Calculate the rental points based on the price code."""
        return self.price_code.get_rental_points(self.days_rented)

