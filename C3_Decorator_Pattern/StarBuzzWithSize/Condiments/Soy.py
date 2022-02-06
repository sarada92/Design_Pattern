from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size
from C3_Decorator_Pattern.StarBuzzWithSize.Condiments.Condiments import Condiments


class Soy(Condiments):

    def __init__(self, beverage: Beverages):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soy'

    def cost(self):
        cost = self.beverage.cost()
        size = self.beverage.get_size()
        if size == Size.TALL:
            print("Soy cost", cost + 0.5)
            cost += 0.5
        elif size == Size.GRANDE:
            print("Soy cost", cost + 1.0)
            cost += 1
        elif size == Size.VENTI:
            print("Soy cost", cost + 2.0)
            cost += 2

        return cost
