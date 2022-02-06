from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.PizzaStore.PizzaStore import PizzaStore
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.SimpleFactory.SimplePizzaFactory import SimplePizzaFactory

if __name__ == '__main__':

    # A simple factory object will handle of different Pizza class creation
    factory = SimplePizzaFactory()

    # HBR Layout Hangout Pizza outlet
    hbr_layout = PizzaStore(factory)
    my_pizza = hbr_layout.order_pizza('Veggie')
    print("I have Ordered -", my_pizza.description(), "\n")

    # Kamanahali Hangout Pizza outlet
    kamanahali = PizzaStore(factory)
    jane_pizza = kamanahali.order_pizza('cheese')
    print("Jane Ordered -", jane_pizza.description(), "\n")

    # Martha ordering from HBR Layout
    martha = hbr_layout.order_pizza('pineapple')
    print("Martha has Ordered -", martha.description(), "\n")

    # Duke ordering from Kamanahali Layout
    duke = hbr_layout.order_pizza('mushroom')
    print("duke has Ordered -", duke.description(), "\n")
