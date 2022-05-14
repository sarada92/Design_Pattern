from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza import Pizzeria
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.NYCheesePizza import NYCheesePizza
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.NYMushroomPizza import NYMushroomPizza
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.PizzaStore.PizzaStore import PizzaStore


class NYPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str) -> Pizzeria:
        if pizza_type.lower() == 'cheese':
            return NYCheesePizza()
        elif pizza_type.lower() == 'mushroom':
            return NYMushroomPizza()
