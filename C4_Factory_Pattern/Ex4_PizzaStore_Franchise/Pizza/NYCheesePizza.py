from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.Pizzeria import Pizzeria


class NYCheesePizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'NY Cheese'
        self.dough = 'Thin Crust'
        self.sauce = 'Cheese Pizza Sauce with salty and spicy tomato'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")

    def description(self):
        return 'Cheese Pizza'
