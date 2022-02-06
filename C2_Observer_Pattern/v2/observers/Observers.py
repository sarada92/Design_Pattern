from abc import ABC, abstractmethod, ABCMeta


class Observers(metaclass=ABCMeta):

    # Would cause a circular dependency
    # Which is not allowed
    # During Initialization we will make each observer to subscriber to any one of the Subject
    # @abstractmethod
    # def subscribe_to_subject(self, subject: Subject):
    #     pass

    @abstractmethod
    def update(self):
        pass
