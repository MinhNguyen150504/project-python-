class ShowTime:
    def __init__(self, st_id, movie_id, show_date, show_time, available_seats):
        self.st_id = str(st_id)
        self.movie_id = str(movie_id)
        self.show_date = str(show_date)
        self.show_time = str(show_time)
        self.available_seats = int(available_seats)

    def to_file_string(self):
        """
        Formats the object's attributes as a string separated by '|' 
        for saving to a .txt file.
        """
        return f"{self.st_id}|{self.movie_id}|{self.show_date}|{self.show_time}|{self.available_seats}\n"