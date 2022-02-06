from abc import ABC, ABCMeta, abstractmethod


class Pizzeria(metaclass=ABCMeta):

    @abstractmethod
    def description(self):
        pass

    # All these methods are controlled by Parent class
    # To keep a tight eye on it's pizza making quality
    def prepare_pizza(self):
        name = self.description()
        print("Preparing", name)

    def bake(self):
        name = self.description()
        print("Baking", name)

    def cut(self):
        name = self.description()
        print("Make a cut in", name)

    def box(self):
        name = self.description()
        print("Your pizza is ready, Enjoy", name)
