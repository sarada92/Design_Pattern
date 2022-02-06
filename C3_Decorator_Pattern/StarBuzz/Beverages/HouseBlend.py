from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages


class HouseBlend(Beverages):

    def __init__(self):
        self.description = 'House Blend'

    def cost(self):
        return 0.89
