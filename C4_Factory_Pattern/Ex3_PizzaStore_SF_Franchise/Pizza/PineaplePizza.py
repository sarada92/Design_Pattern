from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria


class PineapplePizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'Pineapple'
        self.dough = 'Regular Crust'
        self.sauce = 'Pineapple Pizza Sauce'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")
        self.toppings.append("Pineapple Slices")

    def description(self):
        return "Pineapple Pizza"
