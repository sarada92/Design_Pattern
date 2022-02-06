from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzz.Condiments.Condiments import Condiments


class Mocha(Condiments):

    def __init__(self, beverage: Beverages):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return self.beverage.cost() + 0.20
