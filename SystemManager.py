from models.Movie import Movie
from models.ShowTime import ShowTime
from models.Booking import Booking


from utils.file_handler import load_from_file, save_to_file

class SystemManager:
    def __init__(self):
        self.movies_list = []
        self.showtimes_list = []
        self.bookings_list = []

    def load_data(self):
        """Loads data from .txt files into the system lists."""
        
        movie_data = load_from_file("movies.txt")
        for row in movie_data:
            if len(row) == 5:
                self.movies_list.append(Movie(row[0], row[1], row[2], row[3], row[4]))
        
        
        showtime_data = load_from_file("showtimes.txt")
        for row in showtime_data:
            if len(row) == 5:
                self.showtimes_list.append(ShowTime(row[0], row[1], row[2], row[3], row[4]))

        
        booking_data = load_from_file("bookings.txt")
        for row in booking_data:
            if len(row) == 5:
                self.bookings_list.append(Booking(row[0], row[1], row[2], row[3], row[4]))

    def save_data(self):
        """Saves current system lists back to .txt files."""
        save_to_file("movies.txt", self.movies_list)
        save_to_file("showtimes.txt", self.showtimes_list)
        save_to_file("bookings.txt", self.bookings_list)

    def add_movie(self, movie_id, title, genre, duration, price):
        
        for movie in self.movies_list:
            if movie.movie_id == movie_id:
                print("Error: Movie ID already exists.")
                return

        try:
            
            new_movie = Movie(movie_id, title, genre, int(duration), float(price))
            self.movies_list.append(new_movie)
            print("Movie added successfully.")
        except ValueError:
            print("Error: Invalid data types for duration or price. Must be numbers.")

    def update_movie(self, movie_id, new_details):
        for movie in self.movies_list:
            if movie.movie_id == movie_id:
                
                if new_details.get('title'):
                    movie.title = new_details['title']
                if new_details.get('genre'):
                    movie.genre = new_details['genre']
                if new_details.get('duration'):
                    try:
                        movie.duration = int(new_details['duration'])
                    except ValueError:
                        print("Warning: Invalid duration format. Duration not updated.")
                if new_details.get('price'):
                    try:
                        movie.ticket_price = float(new_details['price'])
                    except ValueError:
                        print("Warning: Invalid price format. Price not updated.")
                
                print("Movie updated successfully.")
                return True
        print("Error: Movie ID not found.")
        return False

    def delete_movie(self, movie_id):
        
        original_length = len(self.movies_list)
        self.movies_list = [m for m in self.movies_list if m.movie_id != movie_id]
        
        if len(self.movies_list) < original_length:
            
            self.showtimes_list = [st for st in self.showtimes_list if st.movie_id != movie_id]
            print("Movie and associated showtimes deleted.")
        else:
            print("Error: Movie ID not found.")

    def display_movies(self):
        if not self.movies_list:
            print("No movies available.")
            return
        
        print(f"{'ID':<10} | {'Title':<20} | {'Genre':<15} | {'Duration':<10} | {'Price':<10}")
        print("-" * 75)
        for m in self.movies_list:
            print(f"{m.movie_id:<10} | {m.title:<20} | {m.genre:<15} | {m.duration:<10} | ${m.ticket_price:<10.2f}")

    def add_showtime(self, st_id, movie_id, date, time, seats):

        movie_exists = any(m.movie_id == movie_id for m in self.movies_list)
        if not movie_exists:
            print("Error: Movie ID not found.")
            return

        try:
            new_st = ShowTime(st_id, movie_id, date, time, int(seats))
            self.showtimes_list.append(new_st)
            print("Showtime scheduled successfully.")
        except ValueError:
            print("Error: Available seats must be an integer.")

    def book_ticket(self, b_id, st_id, customer_name, qty, date):
        try:
            qty = int(qty)
        except ValueError:
            print("Error: Quantity must be a number.")
            return False

        for st in self.showtimes_list:
            if st.st_id == st_id:
                if qty <= 0:
                    print("Error: Invalid quantity.")
                    return False
                
                if st.available_seats < qty:
                    print(f"Error: Only {st.available_seats} seats left.")
                    return False
                
                st.available_seats -= qty
                
                new_booking = Booking(b_id, st_id, customer_name, qty, date)
                self.bookings_list.append(new_booking)
                print("Booking successful! Seats have been updated.")
                return True
                
        print("Error: Showtime ID not found.")
        return False

    def cancel_booking(self, booking_id):
        for booking in self.bookings_list:
            if booking.booking_id == booking_id:
                
                for st in self.showtimes_list:
                    if st.st_id == booking.st_id:
                        st.available_seats += booking.number_of_tickets
                        break
                
                self.bookings_list.remove(booking)
                print("Booking canceled and seats restored.")
                return
                
        print("Error: Booking ID not found.")

    def search_data(self, keyword, criteria):
        results = []
        if criteria == "title":
            results = [m for m in self.movies_list if keyword.lower() in m.title.lower()]
        elif criteria == "genre":
            results = [m for m in self.movies_list if keyword.lower() in m.genre.lower()]
        else:
            print("Invalid criteria. Use 'title' or 'genre'.")
            return

        if not results:
            print("No matching results found.")
        else:
            print(f"Found {len(results)} matches:")
            for m in results:
                print(f"- [{m.movie_id}] {m.title} ({m.genre})")

    def sort_data(self, key):
        if not self.movies_list:
            print("No movies to sort.")
            return

        if key == "price":
            sorted_movies = sorted(self.movies_list, key=lambda x: x.ticket_price)
        elif key == "duration":
            sorted_movies = sorted(self.movies_list, key=lambda x: x.duration)
        else:
            print("Invalid sort key. Use 'price' or 'duration'.")
            return
            
        print("--- SORTED MOVIES ---")
        for m in sorted_movies:
            print(f"[{m.movie_id}] {m.title} | {key.capitalize()}: {getattr(m, 'ticket_price' if key == 'price' else 'duration')}")