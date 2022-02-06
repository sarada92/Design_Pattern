from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria


class CheesePizza(Pizzeria):

    def __init__(self):
        self.name = 'Cheese'
        self.dough = 'Regular Crust'
        self.sauce = 'Cheese Pizza Sauce'

    def description(self):
        return 'Cheese Pizza'
