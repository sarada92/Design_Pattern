from C2_Observer_Pattern.v1.observers.Observers import Observers
from C2_Observer_Pattern.v1.subject.Subject import Subject


class Forecast(Observers):

    prev_temperature = 0.0
    curr_temperature = 29.92
    humidity = 0
    pressure = 0

    def __init__(self, subject: Subject):
        subject.add_observer(self)

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self, temperature, humidity, pressure):  # What if Subject add one more field in Update? See v2
        self.prev_temperature = self.curr_temperature
        self.curr_temperature = temperature
        self.display()

    def display(self):
        if self.curr_temperature > self.prev_temperature:
            print("It's hotter outside")
        elif self.curr_temperature < self.prev_temperature:
            print('Go out with winter clothes')
        else:
            print("More of the same")
