from abc import ABC, abstractmethod

class ShipmentFactory(ABC):
    @abstractmethod
    def create_shipment(self, weight):
        pass
