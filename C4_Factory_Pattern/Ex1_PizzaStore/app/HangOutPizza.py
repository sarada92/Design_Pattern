from C4_Factory_Pattern.Ex1_PizzaStore.PizzaStore.PizzaStore import PizzaStore

if __name__ == '__main__':
    pizza = PizzaStore()
    my_pizza = pizza.order_pizza('Veggie')
    print(my_pizza)

    martha = pizza.order_pizza('Cheese')
    print(martha)
