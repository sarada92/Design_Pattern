from C1_Startegy_Pattern.behavior.QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):

    def quack(self):
        print("Silent")
