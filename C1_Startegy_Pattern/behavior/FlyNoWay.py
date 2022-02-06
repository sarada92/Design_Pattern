from C1_Startegy_Pattern.behavior.FlyBehavior import FlyBehavior


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly...")
