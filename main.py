import sys
from services.SystemManager import SystemManager

def display_menu():
    """Displays the main menu of the system."""
    print("\n" + "="*50)
    print("      ***MOVIE TICKET BOOKING SYSTEM***       ")
    print("="*50)
    print(" [ MOVIE MANAGEMENT ]")
    print("  1. Add a new Movie")
    print("  2. Update Movie details")
    print("  3. Delete a Movie")
    print("  4. Display all Movies")
    print("-" * 50)
    print(" [ SHOWTIME & BOOKING ]")
    print("  5. Add a Showtime")
    print("  6. Book a Ticket")
    print("  7. Cancel a Booking")
    print("-" * 50)
    print(" [ SEARCH & SORT ]")
    print("  8. Search Data")
    print("  9. Sort Data")
    print("-" * 50)
    print("  0. Save & Exit")
    print("="*50)

def main():
    manager = SystemManager()
    
    print("Starting system and loading data...")
    manager.load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ").strip()

        if choice == '1':
            print("\n--- ADD NEW MOVIE ---")
            movie_id = input("Enter Movie ID: ")
            title = input("Enter Title: ")
            genre = input("Enter Genre (e.g., Action, Comedy): ")
            duration = input("Enter Duration (minutes): ")
            price = input("Enter Ticket Price: ")
            manager.add_movie(movie_id, title, genre, duration, price)
        
        elif choice == '2':
            print("\n--- UPDATE MOVIE ---")
            movie_id = input("Enter Movie ID to update: ")
            print("Enter new details (press Enter to skip keeping the old value):")
            title = input("New Title: ")
            genre = input("New Genre: ")
            duration = input("New Duration (minutes): ")
            price = input("New Ticket Price: ")
            
            new_details = {
                'title': title,
                'genre': genre,
                'duration': duration,
                'price': price
            }
            manager.update_movie(movie_id, new_details)
            
        elif choice == '3':
            print("\n--- DELETE MOVIE ---")
            movie_id = input("Enter Movie ID to delete: ")
            manager.delete_movie(movie_id)

        elif choice == '4':
            print("\n--- MOVIE LIST ---")
            manager.display_movies()

        elif choice == '5':
            print("\n--- ADD SHOWTIME ---")
            st_id = input("Enter Showtime ID: ")
            movie_id = input("Enter Movie ID for this showtime: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            time = input("Enter Time (HH:MM): ")
            seats = input("Enter available seats: ")
            manager.add_showtime(st_id, movie_id, date, time, seats)

        elif choice == '6':
            print("\n--- BOOK TICKET ---")
            b_id = input("Enter new Booking ID: ")
            st_id = input("Enter Showtime ID: ")
            customer_name = input("Enter Customer Name: ")
            qty = input("Enter number of tickets to book: ")
            date = input("Enter Booking Date (YYYY-MM-DD): ")
            manager.book_ticket(b_id, st_id, customer_name, qty, date)
            
        elif choice == '7':
            print("\n--- CANCEL BOOKING ---")
            b_id = input("Enter Booking ID to cancel: ")
            manager.cancel_booking(b_id)

        elif choice == '8':
            print("\n--- SEARCH DATA ---")
            criteria = input("Search by (title/genre): ").strip().lower()
            keyword = input("Enter keyword: ")
            manager.search_data(keyword, criteria)

        elif choice == '9':
            print("\n--- SORT DATA ---")
            key = input("Sort movies by (price/duration): ").strip().lower()
            manager.sort_data(key)

        elif choice == '0':
            print("\nSaving data...")
            manager.save_data()
            print("Data saved successfully. Goodbye!")
            sys.exit()
            
        else:
            print("\n[Error] Invalid choice. Please enter a number between 0 and 9.")
            
if __name__ == "__main__":
    main()
