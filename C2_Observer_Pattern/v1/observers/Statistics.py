from C2_Observer_Pattern.v1.observers.Observers import Observers
from C2_Observer_Pattern.v1.subject.Subject import Subject


class Statistics(Observers):

    max_temperature = 0.0
    humidity = 0
    pressure = 0

    least_temperature = 200.0
    total_days_reading = 0
    total_temp_sum = 0.0

    def __init__(self, subject: Subject):
        subject.add_observer(self)

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self, temperature, humidity, pressure):

        # Finding Avg/Max/Min temperature
        self.total_days_reading += 1
        self.total_temp_sum += temperature

        self.max_temperature = max(self.max_temperature, temperature)
        self.least_temperature = min(temperature, self.least_temperature)

        self.humidity = humidity
        self.pressure = pressure

        self.display()

    def display(self):
        self.total_days_reading = 1 if self.total_days_reading == 0 else self.total_days_reading
        print("Min Temperature - ", self.least_temperature,
              "\nMax Temperature - ", self.max_temperature,
              "\nAvg Temperature - ", self.total_temp_sum / self.total_days_reading)
