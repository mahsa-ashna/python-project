#import User

class user :
    def __init__(self, date, time, location, price, capacity, remaining_capacity):
        self.date = date
        self.time = time
        self.location = location
        self.price = price
        self.capacity = capacity
        self.remaining_capacity = remaining_capacity

    def ticket(self, ticket):
        pass

    def __str__(self):
        return f"{self.date} is date"

