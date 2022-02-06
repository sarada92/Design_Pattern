from C1_Startegy_Pattern.behavior.FlyBehavior import FlyBehavior
from C1_Startegy_Pattern.behavior.FlyNoWay import FlyNoWay
from C1_Startegy_Pattern.behavior.FlyWithWings import FlyWithWings
from C1_Startegy_Pattern.objects.MallardDuck import MallardDuck


if __name__ == '__main__':
    mallard = MallardDuck()
    print("Printing Default Behavior")
    mallard.perform_fly()
    mallard.perform_quack()

    print("\nAfter Changing default Behavior")
    mallard.set_fly_behavior(FlyNoWay())
    mallard.perform_fly()
    mallard.perform_quack()
    # print(issubclass(FlyNoWay, FlyBehavior))
