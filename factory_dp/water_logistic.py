from logistics import Logistics

class SmallShip(Logistics):
    def ship_product(self):
        print("ship via small ship")


class LargeShip(Logistics):
    def ship_product(self):
        print("ship via large ship")