from abc import ABC, ABCMeta, abstractmethod


class Beverages(metaclass=ABCMeta):

    description = ''

    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass
