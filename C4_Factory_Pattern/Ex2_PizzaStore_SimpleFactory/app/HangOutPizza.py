from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.PizzaStore.PizzaStore import PizzaStore
from C4_Factory_Pattern.Ex2_PizzaStore_SimpleFactory.SimpleFactory.SimplePizzaFactory import SimplePizzaFactory

if __name__ == '__main__':

    # A simple factory object will handle of different Pizza class creation
    factory = SimplePizzaFactory()

    pizza = PizzaStore(factory)
    my_pizza = pizza.order_pizza('Veggie')
    print("I have Ordered -", my_pizza.description(), "\n")

    martha = pizza.order_pizza('Mushroom')
    print("Martha has Ordered -", martha.description(), "\n")
