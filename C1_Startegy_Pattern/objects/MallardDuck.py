from C1_Startegy_Pattern.behavior.FlyWithWings import FlyWithWings
from C1_Startegy_Pattern.behavior.Quack import Quack
from C1_Startegy_Pattern.objects.Duck import Duck


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self._flyBehavior = FlyWithWings()
        self._quackBehavior = Quack()
