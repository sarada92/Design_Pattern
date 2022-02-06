from C2_Observer_Pattern.v2.observers.Observers import Observers
from C2_Observer_Pattern.v2.subject.Subject import Subject
from C2_Observer_Pattern.v2.subject.WeatherData import WeatherData


class HeatIndex(Observers):
    index = 0
    temperature = 0.0
    humidity = 0

    def __init__(self, subject: WeatherData):
        subject.add_observer(self)
        self.subject = subject

    def update(self):
        self.temperature = self.subject.get_temperature()
        self.humidity = self.subject.get_humidity()

        self.compute_heat_index(self.temperature, self.humidity)
        self.display()

    def compute_heat_index(self, t, rh):
        self.index = (((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
                        + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh))
                        + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                        (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                                                                                            (rh * rh * rh)) + (
                                0.00000142721 * (t * t * t * rh)) +
                        (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                        0.000000000843296 * (t * t * rh * rh * rh)) -
                       (0.0000000000481975 * (t * t * t * rh * rh * rh))))

    def display(self):
        print("Heat Index -", self.index)
