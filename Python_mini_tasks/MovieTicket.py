class MovieTicket:
    def __init__(self, booked):
        self.booked = booked

    def total_booked(self):
        return len(self.booked)

    def seat_booked(self, seat):
        return seat in self.booked

    def available_seats(self):
        available = []

        for i in range(1, 21):
            if i not in self.booked:
                available.append(i)

        return available


booked = list(map(int, input("Booked Seats: ").split()))

m = MovieTicket(booked)
print("Total Booked Seats:", m.total_booked())
print("Available Seats:", m.available_seats())