from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages


class Decaf(Beverages):

    def __init__(self):
        self.description = 'Decaf'

    def cost(self):
        return 1.05
