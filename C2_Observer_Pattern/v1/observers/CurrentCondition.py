from C2_Observer_Pattern.v1.observers.Observers import Observers
from C2_Observer_Pattern.v1.subject.Subject import Subject


class CurrentCondition(Observers):

    temperature = 0.0
    humidity = 0
    pressure = 0

    def __init__(self, subject: Subject):
        subject.add_observer(self)

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def display(self):
        print("Current Temperature - ", self.temperature, "\nHumidity - ", self.humidity, "\nPressure - ", self.pressure)
