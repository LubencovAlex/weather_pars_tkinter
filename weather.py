
# Экземпляр класса с погодой

class Weather:

    def __init__(self, city_name, current_time, temp_current, details, presure, wind, humidity):
        self.city_name = city_name
        self.current_time = current_time
        self.temp_current = temp_current
        self.details = details
        self.presure = presure
        self.wind = wind
        self.humidity = humidity