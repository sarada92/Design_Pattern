from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.Pizzeria import Pizzeria


class ChicagoMushroomPizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Mushroom'
        self.dough = 'Regular Crust'
        self.sauce = 'Mushroom Pizza Sauce + Rich Tomato'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")
        self.toppings.append("Mushroom Slices")

    def description(self):
        return 'Mushroom Pizza'
