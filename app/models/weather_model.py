class Weather:
    def __init__(self, temp, humidity, timestamp):
        self.temp = temp
        self.humidity = humidity
        self.timestamp = timestamp

    def __str__(self):
        return f"Temp: {self.temp}, Humidity: {self.humidity}, Time: {self.timestamp}"