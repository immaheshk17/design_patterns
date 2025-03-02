from abc import ABC, abstractmethod

class Logistics(ABC):
    @abstractmethod
    def ship_product(self):
        pass