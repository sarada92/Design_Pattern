from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Beverages import Beverages
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size


class HouseBlend(Beverages):

    def get_description(self):
        return 'House Blend'

    def cost(self):
        cost = 0.89
        size = self.get_size()
        if size == Size.TALL:
            return cost + 0.0
        elif size == Size.GRANDE:
            return cost + 1.0
        elif size == Size.VENTI:
            return cost + 2.0
