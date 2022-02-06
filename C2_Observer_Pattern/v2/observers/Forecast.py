from C2_Observer_Pattern.v2.observers.Observers import Observers
from C2_Observer_Pattern.v2.subject.Subject import Subject
from C2_Observer_Pattern.v2.subject.WeatherData import WeatherData


class Forecast(Observers):

    subject = None
    prev_temperature = 0.0
    curr_temperature = 29.92
    humidity = 0
    pressure = 0

    def __init__(self, subject: WeatherData):
        subject.add_observer(self)
        self.subject = subject

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self):
        self.prev_temperature = self.curr_temperature
        self.curr_temperature = self.subject.get_temperature()
        self.display()

    def display(self):
        if self.curr_temperature > self.prev_temperature:
            print("It's hotter outside")
        elif self.curr_temperature < self.prev_temperature:
            print('Go out with winter clothes')
        else:
            print("More of the same")
