from C4_Factory_Pattern.Ex4_PizzaStore_Franchise.PizzaStore.NYPizzaStore import NYPizzaStore

if __name__ == '__main__':

    ny = NYPizzaStore()

    # Marry Ordered Mushroom pizza
    marry = ny.order_pizza('mushroom')
    print("Marry Ordered -", marry.description())
    