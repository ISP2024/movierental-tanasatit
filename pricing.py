from abc import ABC, abstractmethod
from enum import Enum


class PriceCode(Enum):
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instances = {}  # Store one instance per class

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls)
        return cls._instances[cls]

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

