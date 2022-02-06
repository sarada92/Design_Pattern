from abc import ABC, ABCMeta, abstractmethod
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Beverages import Beverages


class Condiments(Beverages, ABC):

    beverage: Beverages

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    # Do the recursive search, Try with out this function
    # One of the best example of recursion evaluation
    def get_size(self):
        return self.beverage.get_size()
