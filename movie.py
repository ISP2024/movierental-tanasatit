from typing import Collection
from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def get_title(self) -> str:
        return self.title

    def is_genre(self, genre_name) -> bool:
        return genre_name in (g for g in self.genre)

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    """
    Singleton class for managing a movie catalog.
    Loads movies from a CSV file and provides access to Movie objects.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._movies = []
            cls._instance._load_movies_from_csv('movies.csv')
        return cls._instance

    def _load_movies_from_csv(self, filename: str):
        """Load movies from a CSV file using pandas"""
        data = pd.read_csv(filename, header=0)

        for _, row in data.iterrows():
            title = row['title']
            year = row['year']

            genres = row['genres'].split('|') if not pd.isna(row['genres']) else []
            movie = Movie(title, year, genres)
            self._movies.append(movie)

    def get_movie(self, title: str, year: int = None):
        """Return the movie with the given title and optional year."""
        for movie in self._movies:
            if movie.title == title and (year is None or movie.year == year):
                return movie
        return None
