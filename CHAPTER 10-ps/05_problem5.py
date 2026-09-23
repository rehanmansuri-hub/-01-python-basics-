# Create a Train class
class Train:

    # Constructor
    def __init__(self, train_name, seats, fare):
        self.train_name = train_name
        self.seats = seats
        self.fare = fare

    # Method to book a ticket
    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats available.")

    # Method to show train status
    def get_status(self):
        print("Train:", self.train_name)
        print("Available seats:", self.seats)

    # Method to show fare
    def get_fare(self):
        print("Train:", self.train_name)
        print("Fare:", self.fare)


# Create a Train object
train = Train("Indore Express", 5, 500)

# Show train status
train.get_status()

# Show fare
train.get_fare()

# Book a ticket
train.book_ticket()

# Show updated status
train.get_status()