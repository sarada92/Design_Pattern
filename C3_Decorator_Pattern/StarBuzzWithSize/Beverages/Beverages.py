from abc import ABC, ABCMeta, abstractmethod
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size


class Beverages(metaclass=ABCMeta):

    description = ''
    size = Size.TALL

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    def get_size(self):
        return self.size

    def set_size(self, size: Size):
        self.size = size
