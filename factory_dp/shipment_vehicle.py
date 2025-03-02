
from factory import ShipmentFactory
from road_logistic import Car, Truck
from water_logistic import LargeShip, SmallShip
from air_logistic import Boing225, Boing115

class RoadFactory(ShipmentFactory):
    def create_shipment(self, weight):
        if weight < 10:
            return Car()
        return Truck()

class WaterFactory(ShipmentFactory):
    def create_shipment(self, weight):
        if weight < 10:
            return SmallShip()
        return LargeShip()


class AirFactory(ShipmentFactory):
    def create_shipment(self, weight):
        if weight < 10:
            return Boing115()
        return Boing225()

