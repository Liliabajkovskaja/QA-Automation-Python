class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if self.number >= 1:
            if len(self.passengers) < 10:
                self.passengers.append(passenger)
                print(f"Passenger {len(self.passengers)} is added to {self.number} wagon")
            else:
                print(f"Wagon {self.number} is full. Passenger {passenger} cannot be added.")
        else:
            print("No wagon exists. Cannot add passenger.")

    def __len__(self):
        print(f"Count passengers: {len(self.passengers)}")
        return len(self.passengers)

    def __str__(self):
        return f"{self.number}"
