from abc import abstractmethod
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.Pizzeria import Pizzeria


class PizzaStore:

    pizza: Pizzeria

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

    # You can order your favourite pizza from one of the pizza store
    def order_pizza(self, pizza_type: str) -> Pizzeria:
        # Different Pizza type class creation burden is now taken by SimplePizzaFactory Class
        self.pizza = self.create_pizza(pizza_type)
        self.pizza.prepare_pizza()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza
