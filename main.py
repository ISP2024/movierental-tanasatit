from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer
from pricing import *


def make_movies():
    """Some sample movies."""
    catalog = MovieCatalog()
    movies = [
        Movie("Air", 2024, 'Drama'),
        catalog.get_movie('Oppenheimer'),
        Movie('Frozen', 2013, 'Children'),
        catalog.get_movie('Bitconned'),
        catalog.get_movie('Particle Fever')
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())