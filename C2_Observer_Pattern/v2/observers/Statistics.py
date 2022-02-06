from C2_Observer_Pattern.v2.subject.WeatherData import WeatherData
from C2_Observer_Pattern.v2.observers.Observers import Observers
from C2_Observer_Pattern.v1.subject.Subject import Subject


class Statistics(Observers):

    subject = None
    temperature = 0.0
    max_temperature = 0.0

    least_temperature = 200.0
    total_days_reading = 0
    total_temp_sum = 0.0

    def __init__(self, subject: WeatherData):
        subject.add_observer(self)
        self.subject = subject

    # def subscribe_to_subject(self, subject: Subject):
    #     subject.add_observer(self)

    def update(self):

        self.temperature = self.subject.get_temperature()

        # Finding Avg/Max/Min temperature
        self.total_days_reading += 1
        self.total_temp_sum += self.temperature

        self.max_temperature = max(self.max_temperature, self.temperature)
        self.least_temperature = min(self.temperature, self.least_temperature)


        self.display()

    def display(self):
        self.total_days_reading = 1 if self.total_days_reading == 0 else self.total_days_reading
        print("Min Temperature - ", self.least_temperature,
              "\nMax Temperature - ", self.max_temperature,
              "\nAvg Temperature - ", self.total_temp_sum / self.total_days_reading)
