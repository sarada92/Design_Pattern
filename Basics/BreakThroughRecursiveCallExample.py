import enum
from abc import ABC, ABCMeta


# Different Size of beverages
class Size(enum.Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


# Abstract Beverage class
# Get Size to return size of beverage
class Beverages(ABC):
    size = Size.TALL

    def get_size(self):
        print(self.size)

    def set_size(self, size: Size):
        self.size = size


class Condiments(Beverages, metaclass=ABCMeta):
    def get_description(self):
        print("Condiments added ...")


class Espresso(Beverages):
    def get_details(self):
        print("I am espresso")


class Mocha(Condiments):
    def __init__(self, beverage: Beverages):
        self.beverage = beverage


class Soy(Condiments):
    def __init__(self, beverage: Beverages):
        self.beverage = beverage


if __name__ == "__main__":
    espresso = Espresso()
    espresso.get_size()  # TALL
    espresso.set_size(Size.VENTI)
    espresso.get_size()  # VENTI

    mocha = Mocha(espresso)
    mocha.get_size()  # TALL, Why? Expected is VENTI
    """
    Reason:
    mocha.get_size(), calls Beverage.get_size() directly
    We must call its self.beverage class get_size()
    """
    print("\nClass is")
    print("Mocha object:", mocha.beverage)
    print("espresso object:", espresso)

    print("\nDirectly calling Object to get get_size")
    # here mocha.beverage() object is passed to get_size()
    # hence it return the default size
    mocha.beverage.get_size()
    Espresso().get_size()
    Espresso.get_size(espresso)  # Passing espresso object to get_size

    """
    Till now everything looks good. But how we can make things silk
    Rather following up the length approach.
    Ex: what if the below code we want to do the same
    """
    print("\nDouble Mocha")
    double_mocha = Mocha(mocha)
    double_mocha.get_size()

    print("\nClass is")
    print("Double Mocha beverage object:\t\t\t", double_mocha.beverage)
    print("Mocha object:\t\t\t\t\t\t\t", mocha)
    print("Double Mocha beverage.beverage object:\t", double_mocha.beverage.beverage)
    print("Mocha beverage object:\t\t\t\t\t", mocha.beverage)
    print("Espresso object:\t\t\t\t\t\t", espresso)

    print("\nCalling Class beverage object to get_size for double mocha")
    double_mocha.beverage.beverage.get_size()

    print("\nTriple Mocha")
    triple_mocha = Mocha(double_mocha)
    triple_mocha.get_size()
    triple_mocha.beverage.beverage.beverage.get_size()
    # It seems like a serial calling of each beverage class get_size function


# Making things more readable and clean, Recursive approach
class Condiments2(Beverages, metaclass=ABCMeta):
    beverage: Beverages

    def get_description(self):
        print("Condiments added ...")

    def get_size(self):
        return self.beverage.get_size()


class Mocha2(Condiments2):
    def __init__(self, beverage: Beverages):
        self.beverage = beverage


class Soy2(Condiments2):
    def __init__(self, beverage: Beverages):
        self.beverage = beverage


if __name__ == "__main__":
    print("\n\n----------------------------- Cleaner Code --------------------------------------")
    espresso = Espresso()
    espresso.get_size()  # TALL
    espresso.set_size(Size.VENTI)
    espresso.get_size()  # VENTI

    mocha = Mocha2(espresso)
    mocha.get_size()  # VENTI

    double_mocha = Mocha2(mocha)
    triple_mocha = Mocha2(double_mocha)
    double_mocha.get_size()
    triple_mocha.get_size()

    """
    triple_mocha.get_size() --> Condiment.get_size()
                     --> then, self.beverage.get_size() --- A recursive call
                     --> which is, double_mocha.get_size()
    double_mocha.get_size() --> Condiment.get_size()
                     --> then, self.beverage.get_size() --- A recursive call
                     --> which is, mocha.get_size()
    mocha.get_size() --> Condiment.get_size()
                     --> then, self.beverage.get_size() --- A recursive call
                     --> which is, espresso.get_size()
                     --> ### Final return Size.VENTI

    """
