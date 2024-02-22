from HW_8.Computer import Computer


class Laptop(Computer):  # Наслідування
    def __init__(self, brand, cpu, ram, model, battery_life):
        super().__init__(brand, cpu, ram)
        self.model = model
        self.battery_life = battery_life

    def additional_info(self):  # Поліморфізм
        super().additional_info()
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life}")


laptop = Laptop("HP", "P450", "16GB", "8", "10h")

if __name__ == '__main__':
    laptop.additional_info()
