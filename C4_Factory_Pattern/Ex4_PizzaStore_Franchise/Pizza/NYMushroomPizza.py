from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.Pizzeria import Pizzeria


class NYMushroomPizza(Pizzeria):

    # Different Pizza type has different Dough and toppings
    def __init__(self):
        super().__init__()
        self.name = 'NY Mushroom'
        self.dough = 'Thin Crust'
        self.sauce = 'Mushroom Pizza Sauce + Salty and Spicy Tomato'
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")
        self.toppings.append("Mushroom Slices")

    def description(self):
        return 'Mushroom Pizza'
