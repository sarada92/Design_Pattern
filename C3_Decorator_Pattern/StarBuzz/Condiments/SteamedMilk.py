from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzz.Condiments.Condiments import Condiments


class SteamedMilk(Condiments):

    def __init__(self, beverage: Beverages):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Steamed Milk'

    def cost(self):
        return self.beverage.cost() + 0.10
