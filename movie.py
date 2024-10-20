import csv
import logging
from typing import Collection
from dataclasses import dataclass
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(message)s')


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
        return genre_name.lower() in (g.lower() for g in self.genre)

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
            cls._instance.movies = cls._instance._load_movies('movies.csv')
        return cls._instance

    @classmethod
    def _load_movies(cls, filename: str):
        """Load movies from the CSV file into Movie objects."""
        movies = []
        try:
            with open(filename, 'r') as file:
                next(file)
                for line_number, line in enumerate(file, start=2):  #
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = line.split(',')
                    if len(parts) < 4:
                        logging.error(f"Line {line_number}: Unrecognized format '{line}'")
                        continue

                    try:
                        movie_id = parts[0]
                        title = parts[1]
                        year = int(parts[2])
                        genres = parts[3].split('|')
                        movies.append(Movie(title, year, genres))
                    except (ValueError, IndexError) as e:
                        logging.error(f"Line {line_number}: Unrecognized format '{line}'")
                        continue
        except FileNotFoundError:
            print("Movies file not found.")
        except Exception as e:
            print(f"Error loading movies: {e}")

        return movies

    def get_movie(self, title: str, year: int = None) -> Movie:
        """Return the movie with the given title and optional year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        logging.error(f"Movie {title} not found in catalog. (Year: {year})")
        return None