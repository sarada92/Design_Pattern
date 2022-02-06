from C2_Observer_Pattern.v1.observers.CurrentCondition import CurrentCondition
from C2_Observer_Pattern.v1.observers.Forecast import Forecast
from C2_Observer_Pattern.v1.observers.Statistics import Statistics
from C2_Observer_Pattern.v1.subject.WeatherData import WeatherData

if __name__ == '__main__':
    weather_data = WeatherData()

    curr_condition = CurrentCondition(weather_data)
    stats = Statistics(weather_data)
    forecast = Forecast(weather_data)

    print("\nTemperature has changed - 1")
    weather_data.set_weather(10.2, 23, 45)

    print("\nTemperature has changed - 2")
    weather_data.set_weather(12.34, 29, 48)
