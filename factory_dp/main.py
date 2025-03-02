from shipment_vehicle import *

if __name__ == "__main__":
    weight = 20
    road = RoadFactory()
    road.create_shipment(weight).ship_product()

    weight = 9
    water = WaterFactory()
    water.create_shipment(weight).ship_product()

    air = AirFactory()
    air.create_shipment(weight).ship_product()

