from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.Pizza.Pizzeria import Pizzeria


class MushroomPizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'Mushroom'
        self.dough = 'Regular Crust'
        self.sauce = 'Mushroom Pizza Sauce'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")
        self.toppings.append("Mushroom Slices")

    def description(self):
        return 'Mushroom Pizza'
