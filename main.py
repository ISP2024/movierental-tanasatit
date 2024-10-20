# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie,MovieCatalog
from rental import Rental
from customer import Customer
from pricing import PriceCode  # Make sure to import PriceCode if needed


def create_sample_movies(movie_catalog):
    """Add sample movies to the catalog."""
    sample_movies = [
        Movie("The Arrival", 1996, ["Action", "Sci-Fi", "Thriller"]),
        Movie("Cinderella", 1950, ["Animation", "Children", "Musical"]),
        Movie("Mulan", 1998, ["Animation", "Action", "Children"]),
        Movie("Oppenheimer", 2023, ["Biography", "Drama", "History"]),
        Movie("Barbie", 2023, ["Adventure", "Comedy", "Fantasy"]),
    ]

    for movie in sample_movies:
        movie_catalog.get_movie(movie)


if __name__ == '__main__':
    # Create a movie catalog and add sample movies
    movie_catalog = MovieCatalog()
    create_sample_movies(movie_catalog)

    # Create a customer
    customer = Customer("Edward Snowden")

    # Create rentals for the customer using get_movie
    days = 1
    for title, year in [("The Arrival", 1996), ("Cinderella", 1950),
                        ("Mulan", 1998), ("Oppenheimer", 2023),
                        ("Barbie", 2023)]:
        movie = movie_catalog.get_movie(title, year)
        rental = Rental(movie, days, Rental.price_code_for_movie(movie))
        customer.add_rental(rental)
        days = (days + 2) % 5 + 1  # Varying rental days

    # Print the customer's rental statement
    print(customer.statement())
