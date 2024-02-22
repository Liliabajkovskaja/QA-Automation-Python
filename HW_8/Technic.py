from abc import ABC, abstractmethod


class Technic(ABC):  # Абстракція
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def additional_info(self):  # Абстрактний метод
        pass
