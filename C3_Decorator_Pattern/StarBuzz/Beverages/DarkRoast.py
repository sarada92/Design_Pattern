from C3_Decorator_Pattern.StarBuzz.Beverages.Beverages import Beverages


class DarkRoast(Beverages):

    def __init__(self):
        super().__init__()
        self.description = 'Dark Roast'

    def cost(self):
        return 0.99
