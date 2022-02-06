from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size


class Espresso(Beverages):

    def get_description(self):
        return 'Espresso'

    def cost(self):
        cost = 1.99
        size = self.get_size()
        if size == Size.TALL:
            print("Espresso cost", cost + 0.0)
            return cost + 0.0
        elif size == Size.GRANDE:
            print("Espresso cost", cost + 1.0)
            return cost + 1.0
        elif size == Size.VENTI:
            print("Espresso cost", cost + 2.0)
            return cost + 2.0
