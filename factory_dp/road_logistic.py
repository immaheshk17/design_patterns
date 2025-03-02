from logistics import Logistics

class Truck(Logistics):
    def ship_product(self):
        print("ship via truck")


class Car(Logistics):
    def ship_product(self):
        print("ship via car")