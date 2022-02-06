from abc import ABC, ABCMeta, abstractmethod


class Pizzeria(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None

    @abstractmethod
    def description(self):
        pass

    # All these methods are controlled by Parent class
    # To keep a tight eye on it's pizza making quality
    def prepare_pizza(self):
        print("Preparing", self.name)

    def bake(self):
        print("Baking for 20 min")

    def cut(self):
        print("Make a cut in...")

    def box(self):
        print("Your pizza is ready, Boxing Now.")
