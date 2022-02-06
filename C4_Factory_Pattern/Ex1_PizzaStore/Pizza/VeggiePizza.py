from C4_Factory_Pattern.Ex1_PizzaStore.Pizza.Pizzeria import Pizzeria


class VeggiePizza(Pizzeria):

    def __init__(self):
        super().__init__()
        self.name = 'Veggie'
        self.dough = 'Regular Crust'
        self.sauce = 'Veggie Pizza Sauce'
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")

    def description(self):
        return 'Veggie Delight Pizza'
