from pizza_addons import PizzaAddon


class Paneer(PizzaAddon):
    def get_price(self):
        return self.pizza.get_price() + 50 

