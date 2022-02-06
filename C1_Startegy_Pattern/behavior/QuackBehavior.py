from abc import ABC, abstractmethod, ABCMeta


class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass
