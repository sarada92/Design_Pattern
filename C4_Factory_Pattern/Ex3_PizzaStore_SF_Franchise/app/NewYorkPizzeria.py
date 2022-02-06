from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.PizzaStore.PizzaStore import PizzaStore
from C4_Factory_Pattern.Ex3_PizzaStore_SF_Franchise.SimpleFactory.NYSimpleFactory import NYSimpleFactory

if __name__ == '__main__':

    ny_factory = NYSimpleFactory()

    # Marry Ordered Mushroom pizza
    ny_pizza = PizzaStore(ny_factory)
    marry = ny_pizza.order_pizza('mushroom')
    print("Marry Ordered -", marry.description())
    