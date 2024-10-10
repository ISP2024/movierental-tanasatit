import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """
        Test fixture contains:
        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.children_movie = Movie("Frozen", Movie.CHILDREN)

    def test_total_charge(self):
        """ Test total rental price calculation for multiple rentals."""
        self.c.add_rental(Rental(self.new_movie, 1))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.children_movie, 3))
        total_amount = self.c.get_total_charge()
        self.assertEqual(total_amount, 9.5)

        self.c.add_rental(Rental(self.new_movie, 5))
        self.c.add_rental(Rental(self.regular_movie, 3))
        total_amount = self.c.get_total_charge()
        self.assertEqual(total_amount, 28)

    def test_total_rental_points(self):
        """ Test total rental point calculation for multiple rentals."""
        self.c.add_rental(Rental(self.new_movie, 1))
        self.c.add_rental(Rental(self.regular_movie, 4))
        self.c.add_rental(Rental(self.children_movie, 3))
        total_point = self.c.get_total_rental_points()
        self.assertEqual(total_point, 3)

        self.c.add_rental(Rental(self.new_movie, 5))
        self.c.add_rental(Rental(self.regular_movie, 3))
        total_point = self.c.get_total_rental_points()
        self.assertEqual(total_point, 9)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
