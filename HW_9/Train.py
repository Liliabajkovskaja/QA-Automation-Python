from HW_9.Wagon import Wagon


class Train:
    def __init__(self):
        self.wagons = [Wagon(0)]  # locomotive

    def add_wagon(self, wagon):
        self.wagons.append(wagon)
        print(f"Wagon {wagon.number} is added to train")

    def __len__(self):
        count_wagons = len(self.wagons) - 1  # count wagons without locomotive
        return count_wagons

    def __str__(self):
        wagon_numbers = '-'.join([f"[{wagon}]" for wagon in self.wagons[1:]])
        return f"<=[HEAD]-{wagon_numbers}"


train = Train()

wagon1 = Wagon(1)
wagon2 = Wagon(2)
wagon3 = Wagon(3)
locomotive = Wagon(0)

train.add_wagon(wagon1)
train.add_wagon(wagon2)
train.add_wagon(wagon3)

print("*" * 20)
locomotive.add_passenger("some")
wagon1.add_passenger("first")
wagon1.add_passenger("second")
wagon1.add_passenger("third")
wagon1.add_passenger("fourth")

wagon2.add_passenger("first")
print("*" * 20)

print(f"Wagon {wagon1.number} has {len(wagon1.passengers)} passengers")
print("*" * 20)
print(f"Train has {len(train)} wagons")
print(train)
