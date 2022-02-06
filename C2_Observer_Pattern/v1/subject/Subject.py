from abc import abstractmethod, ABCMeta

from C2_Observer_Pattern.v1.observers.Observers import Observers


class Subject(metaclass=ABCMeta):

    @abstractmethod
    def add_observer(self, observer: Observers):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observers):
        pass

    @abstractmethod
    def notify_update(self):
        pass

    @abstractmethod
    def set_weather(self, temperature, humidity, pressure):
        pass

