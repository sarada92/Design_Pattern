from abc import ABC, ABCMeta, abstractmethod


class Condiments(metaclass=ABCMeta):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass
