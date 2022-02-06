from abc import ABC, abstractmethod, ABCMeta


class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass

