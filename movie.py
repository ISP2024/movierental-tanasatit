import logging
from price import *


class Movie:
    """
    A movie available for rent.
    """
    # # The types of movies (price_code).
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code
        self.set_price_code(price_code)

    def set_price_code(self, price_code):
        if price_code == self.REGULAR:
            self.price_strategy = RegularPrice()
        elif price_code == self.NEW_RELEASE:
            self.price_strategy = NewRelease()
        elif price_code == self.CHILDREN:
            self.price_strategy = ChildrensPrice()
        else:
            log = logging.getLogger()
            log.error(f"Movie {self.title} has unrecognized priceCode {price_code}")
            raise ValueError("Invalid price code")

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self, days: int) -> float:
        # get the price code
        return self.price_strategy.get_price(days)

    def get_rental_points(self, days: int) -> int:
        return self.price_strategy.get_rental_points(days)

    def get_title(self) -> str:
        return self.title

    def __str__(self):
        return self.title
