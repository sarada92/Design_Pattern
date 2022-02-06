from C2_Observer_Pattern.v2.observers.Observers import Observers
from C2_Observer_Pattern.v2.subject.Subject import Subject


class WeatherData(Subject):
    observer_list = []
    temperature = 0.0
    humidity = 0
    pressure = 0.0

    def add_observer(self, observer: Observers):
        self.observer_list.append(observer)

    def remove_observer(self, observer: Observers):
        self.observer_list.remove(observer)

    def notify_update(self):
        for observer in self.observer_list:
            observer.update()

    def set_weather(self, temperature, humidity, pressure):  # Class specific Set, Other class might have different
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notify_update()

    def get_temperature(self) -> float:
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure
