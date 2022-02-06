from C2_Observer_Pattern.v2.observers.Observers import Observers
from C2_Observer_Pattern.v2.subject.WeatherData import WeatherData


class CurrentCondition(Observers):

    subject = None
    temperature = 0.0
    humidity = 0
    pressure = 0

    def __init__(self, subject: WeatherData):
        subject.add_observer(self)
        self.subject = subject

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self):

        self.temperature = self.subject.get_temperature()
        self.humidity = self.subject.get_humidity()
        self.pressure = self.subject.get_pressure()

    def display(self):
        print("Current Temperature - ", self.temperature, "\nHumidity - ", self.humidity, "\nPressure - ", self.pressure)
