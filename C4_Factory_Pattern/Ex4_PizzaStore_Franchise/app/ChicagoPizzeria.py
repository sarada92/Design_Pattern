from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.PizzaStore.ChicagoPizzaStore import ChicagoPizzaStore

if __name__ == '__main__':

    # Chicago Pizza Store
    chicago = ChicagoPizzaStore()

    # Dexter Ordered Pineapple Pizza
    dexter = chicago.order_pizza('mushroom')
    print("Dexter Ordered -", dexter.description())
    