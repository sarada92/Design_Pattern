from C3_Decorator_Pattern.StarBuzz.Beverages.Decaf import Decaf
from C3_Decorator_Pattern.StarBuzz.Beverages.Espresso import Espresso
from C3_Decorator_Pattern.StarBuzz.Condiments.Mocha import Mocha
from C3_Decorator_Pattern.StarBuzz.Condiments.Soy import Soy
from C3_Decorator_Pattern.StarBuzz.Condiments.Whip import Whip

if __name__ == '__main__':
    # Double Mocha Espresso
    espresso = Espresso()        # 1.99
    mocha = Mocha(espresso)      # 0.20
    double_mocha = Mocha(mocha)  # 0.20

    print(double_mocha.cost())   # 1.99 + 0.20 + 0.20

    # Decaf with Soy and Whip
    order = Whip(Soy(Decaf()))
    print(order.get_description() + ' $' + str(order.cost()))    # 1.05 + 0.15 + 0.10

    order = Soy(Soy(Decaf()))
    print(order.cost())
