from cheese import Cheese
from paneer import Paneer
from pizza import Pizza

if __name__ == "__main__":
    pizza = Pizza()
    paneer_pizza = Paneer(pizza)

    cheese_paneer_pizza = Cheese(paneer_pizza)

    print(cheese_paneer_pizza.get_price())
