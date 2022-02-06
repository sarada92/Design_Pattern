from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages


class Espresso(Beverages):

    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99
