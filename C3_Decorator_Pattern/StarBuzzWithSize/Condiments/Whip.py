from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size
from C3_Decorator_Pattern.StarBuzzWithSize.Condiments.Condiments import Condiments


class Whip(Condiments):

    def __init__(self, beverage: Beverages):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        cost = 0.10
        size = self.beverage.get_size()
        if size == Size.TALL:
            cost += 0
        elif size == Size.GRANDE:
            cost += 1
        elif size == Size.VENTI:
            cost += 2

        return self.beverage.cost() + cost
