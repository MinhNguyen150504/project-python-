class Booking:
    def __init__(self, booking_id, st_id, customer_name, number_of_tickets, booking_date):
        self.booking_id = str(booking_id)
        self.st_id = str(st_id)
        self.customer_name = str(customer_name)
        self.number_of_tickets = int(number_of_tickets)
        self.booking_date = str(booking_date)

    def to_file_string(self):
        """
        Formats the object's attributes as a string separated by '|' 
        for saving to a .txt file.
        """
        return f"{self.booking_id}|{self.st_id}|{self.customer_name}|{self.number_of_tickets}|{self.booking_date}\n"