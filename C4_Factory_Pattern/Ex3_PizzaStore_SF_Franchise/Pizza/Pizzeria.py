from abc import ABC, ABCMeta, abstractmethod


class Pizzeria(metaclass=ABCMeta):

    # Extended class will set these variables
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

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

    def get_name(self):
        name = self.description()
        print("Your Pizza is in Process...", name)

    def __str__(self):
        desc = self.description()
        print("\n----------------------", desc, "----------------------")
        print(self.dough)
        print(self.sauce)
        for topping in self.toppings:
            print(topping)
        return self.name + "\n"
