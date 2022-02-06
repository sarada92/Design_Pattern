from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.CheesePizza import CheesePizza
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.MushroomPizza import MushroomPizza
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.PineaplePizza import PineapplePizza
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.Pizzeria import Pizzeria
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.VeggiePizza import VeggiePizza


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
