from abc import ABC, abstractmethod
from datetime import datetime

class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instances = {}  # Store one instance per class

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls)
        return cls._instances[cls]

    @classmethod
    def price_code_for_movie(cls, movie):
        """Determine the price strategy for a given movie."""
        current_year = datetime.now().year
        if movie.year == current_year:
            return NewRelease()
        elif any(genre.lower() == "children" or genre.lower() == 'childrens' for genre in movie.genre):
            return ChildrensPrice()
        else:
            return RegularPrice()

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days):
        return 3 * days

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return 1


class ChildrensPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days):
        """New release rentals earn 1 point for each day rented."""
        return 1

