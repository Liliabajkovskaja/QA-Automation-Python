from HW_8.Computer import Computer


class Desktop(Computer):  # Наслідування
    def __init__(self, brand,  cpu, ram,  gpu):
        super().__init__(brand, cpu, ram)
        self.gpu = gpu


    def additional_info(self):  # Поліморфізм
        super().additional_info()
        print(f"GPU: {self.gpu}")


computer_desktop = Desktop("HP",  "Intel i7", "16GB", "Nvidia")

if __name__ == '__main__':
    computer_desktop.additional_info()
