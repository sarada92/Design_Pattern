from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.PizzaStore.PizzaStore import PizzaStore
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.SimpleFactory.ChicagoSimpleFactory import ChicagoSimpleFactory

if __name__ == '__main__':

    # Chicago Factory
    chicago_factory = ChicagoSimpleFactory()

    # Dexter Ordered Pineapple Pizza
    chicago = PizzaStore(chicago_factory)
    dexter = chicago.order_pizza('pineapple')
    print("Dexter Ordered -", dexter.description())
