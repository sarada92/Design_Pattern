from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.Pizza.Pizzeria import Pizzeria


class VeggiePizza(Pizzeria):

    def __init__(self):
        self.name = 'Veggie'
        self.dough = 'Regular Crust'
        self.sauce = 'Veggie Pizza Sauce'

    def description(self):
        return 'Veggie Delight Pizza'
