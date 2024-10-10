import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.children_movie = Movie("Frozen", Movie.CHILDREN)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_price_code())

    def test_rental_price(self):
        """
        Test get_price calculates correct rental price
        based on movie type and rental duration
        """
        # Test new release prices
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        # Test regular movie prices
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

        # Test children movie prices
        rental = Rental(self.children_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """
        Test frequent renter points calculation based on movie type and rental duration.
        """
        rentals = [
            Rental(self.new_movie, 1),
            Rental(self.regular_movie, 4),
            Rental(self.children_movie, 2),
            Rental(self.new_movie, 5),
            Rental(self.regular_movie, 3)
        ]

        total_points = sum(rental.get_rental_points() for rental in rentals)
        self.assertEqual(total_points, 9)


