from HW_8.Technic import Technic


class Computer(Technic):  # Наслідування
    def __init__(self, brand, cpu, ram):
        super().__init__(brand)
        self.cpu = cpu
        self.ram = ram

    def additional_info(self):
        print(f"Brand: {self.brand}")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")


computer = Computer("HP", "P450", "16GB")

if __name__ == '__main__':
    computer.additional_info()
