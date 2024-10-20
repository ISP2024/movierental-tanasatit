import unittest
from rental import Rental
from movie import Movie
from pricing import PriceCode


class PricingTest(unittest.TestCase):

    def test_regular_movie(self):
        """Test the price code for regular movies."""
        movie = Movie("CitizenFour", 2014, ["Documentary"])  # Example movie
        rental = Rental(movie, 3, PriceCode.REGULAR)  # 3 days rental with price code

        self.assertEqual(rental.get_price(), 3.0)  # Adjust based on your pricing logic

    def test_new_release_movie(self):
        """Test the price code for new release movies."""
        movie = Movie("Mulan", 1998, ["Animation", "Family"])  # Example movie
        rental = Rental(movie, 2, PriceCode.NEW_RELEASE)  # 2 days rental with price code

        self.assertEqual(rental.get_price(), 6.0)  # Adjust based on your pricing logic

    def test_childrens_movie(self):
        """Test the price code for children's movies."""
        movie = Movie("Frozen", 2013, ["Animation", "Family"])  # Example movie
        rental = Rental(movie, 5, PriceCode.CHILDREN)  # 5 days rental with price code

        self.assertEqual(rental.get_price(), 4.5)  # Adjust based on your pricing logic
