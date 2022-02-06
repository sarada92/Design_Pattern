from C4_Factory_Pattern.Ex1_PizzaStore.Pizza.CheesePizza import CheesePizza
from C4_Factory_Pattern.Ex1_PizzaStore.Pizza.Pizzeria import Pizzeria
from C4_Factory_Pattern.Ex1_PizzaStore.Pizza.VeggiePizza import VeggiePizza


class PizzaStore:

    pizza: Pizzeria

    # You can order your favourite pizza from one of the pizza store
    def order_pizza(self, pizza_type: str) -> Pizzeria:
        if pizza_type.lower() == 'veggie':
            self.pizza = VeggiePizza()
        elif pizza_type.lower() == 'cheese':
            self.pizza = CheesePizza()

        self.pizza.prepare_pizza()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza
