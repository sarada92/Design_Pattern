from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria


class MushroomPizza(Pizzeria):

    def __init__(self):
        self.name = 'Mushroom'
        self.dough = 'Regular Crust'
        self.sauce = 'Mushroom Pizza Sauce'

    def description(self):
        return 'Mushroom Pizza'
