from typing import Collection
from dataclasses import dataclass


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


