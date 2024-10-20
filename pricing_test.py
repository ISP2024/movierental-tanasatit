import unittest
from pricing import NewRelease, RegularPrice, ChildrensPrice, PriceStrategy
from movie import Movie


class TestPricingStrategy(unittest.TestCase):

    def setUp(self):
        """Set up common variables to use in tests."""
        self.new_release = NewRelease()
        self.regular_price = RegularPrice()
        self.childrens_price = ChildrensPrice()

        # Define reusable movies
        self.movie_new_release = Movie("Avatar", 2024, ['Action'])
        self.movie_children = Movie("Frozen", 2013, ['Children'])
        self.movie_regular = Movie("Inception", 2010, ['Action', 'Thriller'])

    def test_new_release_price(self):
        """Test the pricing and points for New Release movies."""
        days_rented = 5
        self.assertEqual(self.new_release.get_price(days_rented), 15)  # 3 * 5
        self.assertEqual(self.new_release.get_rental_points(days_rented), 5)  # 1 point per day

    def test_regular_price(self):
        """Test the pricing and points for Regular Price movies."""
        days_rented = 1
        self.assertEqual(self.regular_price.get_price(days_rented), 2.0)  # Base price for regular movie
        self.assertEqual(self.regular_price.get_rental_points(days_rented), 1)

        days_rented = 4
        self.assertEqual(self.regular_price.get_price(days_rented), 5.0)  # 2 + 1.5 * (4 - 2)
        self.assertEqual(self.regular_price.get_rental_points(days_rented), 1)

    def test_childrens_price(self):
        """Test the pricing and points for Children's Price movies."""
        days_rented = 2
        self.assertEqual(self.childrens_price.get_price(days_rented), 1.5)  # Base price for children movie
        self.assertEqual(self.childrens_price.get_rental_points(days_rented), 1)

        days_rented = 5
        self.assertEqual(self.childrens_price.get_price(days_rented), 4.5)  # 1.5 + 1.5 * (5 - 3)
        self.assertEqual(self.childrens_price.get_rental_points(days_rented), 1)

    def test_price_code_for_movie(self):
        """Test the price code assignment based on the movie details."""
        price_code = PriceStrategy.price_code_for_movie(self.movie_children)
        self.assertIsInstance(price_code, ChildrensPrice)

        price_code = PriceStrategy.price_code_for_movie(self.movie_new_release)
        self.assertIsInstance(price_code, NewRelease)

        price_code = PriceStrategy.price_code_for_movie(self.movie_regular)
        self.assertIsInstance(price_code, RegularPrice)


