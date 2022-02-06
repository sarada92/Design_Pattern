from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.CheesePizza import CheesePizza
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.MushroomPizza import MushroomPizza
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.PineaplePizza import PineapplePizza
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.VeggiePizza import VeggiePizza


class SimplePizzaFactory:

    pizza: Pizzeria

    def create_pizza(self, pizza_type: str) -> Pizzeria:
        if pizza_type.lower() == 'veggie':
            self.pizza = VeggiePizza()
        elif pizza_type.lower() == 'cheese':
            self.pizza = CheesePizza()
        # Adding two new variety
        elif pizza_type.lower() == 'mushroom':
            self.pizza = MushroomPizza()
        elif pizza_type.lower() == 'pineapple':
            self.pizza = PineapplePizza()

        return self.pizza
