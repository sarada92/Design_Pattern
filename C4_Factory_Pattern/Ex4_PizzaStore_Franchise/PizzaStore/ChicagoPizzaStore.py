from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.ChicagoCheesePizza import ChicagoCheesePizza
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.Pizza.ChicagoMushroomPizza import ChicagoMushroomPizza
from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.PizzaStore.PizzaStore import PizzaStore


# It looks similar as SimpleFactory Method
# But code written wise little different
class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str):
        if pizza_type.lower() == 'cheese':
            return ChicagoCheesePizza()
        elif pizza_type.lower() == 'mushroom':
            return ChicagoMushroomPizza()
