from HW_8.Technic import Technic


class Phone(Technic):  # Наслідування
    def __init__(self, brand, model, screen_size):
        super().__init__(brand)
        self.model = model
        self.screen_size = screen_size

    def additional_info(self):  # Поліморфізм
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Screen Size: {self.screen_size}")


phone = Phone("Samsung", "Galaxy", "6.2 ")

if __name__ == '__main__':
    phone.additional_info()
