from C3_Decorator_Pattern.StarBuzzWithSize.Condiments.Soy import Soy
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Espresso import Espresso
from C3_Decorator_Pattern.StarBuzzWithSize.Beverages.Size import Size
from C3_Decorator_Pattern.StarBuzzWithSize.Condiments.Mocha import Mocha

if __name__ == '__main__':
    # Double Mocha Espresso
    espresso = Espresso()  # 1.99
    mocha = Mocha(espresso)  # 0.20
    double_mocha = Mocha(mocha)  # 0.20
    triple_mocha = Mocha(double_mocha)  # 0.20
    soy = Soy(triple_mocha)

    espresso.set_size(Size.GRANDE)

    print(soy.get_size())
    print(triple_mocha.get_size())
    print(double_mocha.get_size())
    print(mocha.get_size())
    print(espresso.get_size())

    print(soy.get_description() + ' $' + str(soy.cost()))  # 1.99 + 0.20 + 0.20

