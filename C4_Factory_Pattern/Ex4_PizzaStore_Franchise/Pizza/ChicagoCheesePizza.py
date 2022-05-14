from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.Pizzeria import Pizzeria


class ChicagoCheesePizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Cheese'
        self.dough = 'Thick Crust'
        self.sauce = 'Cheese Pizza Sauce with rich tomato'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")

    def description(self):
        return 'Cheese Pizza'
