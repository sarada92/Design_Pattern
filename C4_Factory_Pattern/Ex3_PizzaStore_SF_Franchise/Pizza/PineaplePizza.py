from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria


class PineapplePizza(Pizzeria):

    def __init__(self):
        self.name = 'Pineapple'
        self.dough = 'Regular Crust'
        self.sauce = 'Pineapple Pizza Sauce'

    def description(self):
        return "Pineapple Pizza"
