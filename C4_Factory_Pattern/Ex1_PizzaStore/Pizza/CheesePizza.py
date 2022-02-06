from C4_Factory_Pattern.Ex1_PizzaStore.Pizza.Pizzeria import Pizzeria


class CheesePizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'Cheese'
        self.dough = 'Regular Crust'
        self.sauce = 'Cheese Pizza Sauce'
        self.toppings.append("Fresh Mozzarella");
        self.toppings.append("Parmesan");

    def description(self):
        return 'Cheese Pizza'

