from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.Pizzeria import Pizzeria
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.SimpleFactory.SimplePizzaFactory import SimplePizzaFactory


class PizzaStore:

    pizza: Pizzeria
    factory: SimplePizzaFactory

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    # You can order your favourite pizza from one of the pizza store
    def order_pizza(self, pizza_type: str) -> Pizzeria:

        # Different Pizza type class creation burden is now taken by SimplePizzaFactory Class
        self.pizza = self.factory.create_pizza(pizza_type)

        self.pizza.prepare_pizza()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza
