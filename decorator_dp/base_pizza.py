from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def get_price(self):
        pass
