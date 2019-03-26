import requests
import json
import time

# Download json data
url = 'http://api.openweathermap.org/data/2.5/weather?id=4846834&APPID=f48818a446c345dfa46a2222c9fa1acf&units=imperial'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions
main = weatherData['main']
conditions = weatherData['weather']

class Weather:
    def __init__(self):
        self.temp = int(self.getTemp())
        self.high = int(self.getHigh())
        self.low = int(self.getlow())
        self.condition = self.getConditions()
        self.conditionFile = self.displayConditions()

    def getTemp(self):
        return main['temp']

    def getHigh(self):
        return main['temp_max']

    def getlow(self):
        return main['temp_min']

    def getConditions(self):
        return conditions[0]['main']

    def displayConditions(self):
        if self.getConditions() == "Clouds":
            return "clouds.gif"
        elif self.getConditions() == "Sunny":
            return "sunny.gif"
        elif self.getConditions() == "Partial Clouds":
            return "partial-clouds.gif"
        elif self.getConditions() == "Rain":
            return "rain.gif"
        # add other weather conditions

        # defaults to sun image
        return "sunny.gif"

    def sunrise(self):
        return time.strftime("%I:%M %p", time.localtime(weatherData['sys']['sunrise']))

    def sunset(self):
        return time.strftime("%I:%M %p", time.localtime(weatherData['sys']['sunset']))

    def windSpeed(self):
        return int(weatherData['wind']['speed'])

    def windDirection(self):
        direction = weatherData['wind']['deg']
        if 23 <= direction <= 67:
            return "NE"
        elif 68 <= direction <= 113:
            return "E"
        elif 114 <= direction <= 157:
            return "SE"
        elif 158 <= direction <= 202:
            return "S"
        elif 203 <= direction <= 247:
            return "SW"
        elif 248 <= direction <= 292:
            return "W"
        elif 293 <= direction <= 337:
            return "NE"
        else:
            return "N"
