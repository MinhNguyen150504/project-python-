class Movie:
    def __init__(self, movie_id, title, genre, duration, ticket_price):
        self.movie_id = str(movie_id)
        self.title = str(title)
        self.genre = str(genre)
        self.duration = int(duration)
        self.ticket_price = float(ticket_price)

    def to_file_string(self):
        """
        Formats the object's attributes as a string separated by '|' 
        for saving to a .txt file.
        """
        return f"{self.movie_id}|{self.title}|{self.genre}|{self.duration}|{self.ticket_price}\n"