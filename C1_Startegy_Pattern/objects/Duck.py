from abc import ABC, abstractmethod
from typing import Type
from C1_Startegy_Pattern.behavior.FlyBehavior import FlyBehavior
from C1_Startegy_Pattern.behavior.QuackBehavior import QuackBehavior


class Duck:

    _flyBehavior = None
    _quackBehavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self._flyBehavior.fly()

    def perform_quack(self):
        self._quackBehavior.quack()

    def swim(self):
        print("All ducks can fly, even the decoy!!!")

    def set_fly_behavior(self, fly: Type[FlyBehavior]):
        self._flyBehavior = fly

    def set_quack_behavior(self, quack: Type[QuackBehavior]):
        self._quackBehavior = quack




