class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title):
        # Initialize a new movie. 
        self.title = title

    def get_title(self) -> str:
        return self.title

    def __str__(self):
        return self.title
