import requests
import json
import time

# Download json data
url = 'http://api.openweathermap.org/data/2.5/weather?id=4846834&APPID=f48818a446c345dfa46a2222c9fa1acf&units=imperial'
forecastUrl = 'http://api.openweathermap.org/data/2.5/forecast?id=4846834&APPID=f48818a446c345dfa46a2222c9fa1acf&units=imperial'

response = requests.get(url)
response.raise_for_status()

response1 = requests.get(forecastUrl)

# Load JSON data into a Python variable
weatherData = json.loads(response.text)
#forecastData = json.loads()

# Print weather descriptions
main = weatherData['main']
conditions = weatherData['weather']

class Weather:
    def __init__(self):
        self.temp = "{} °F".format(round(main['temp']))
        self.high = "{} °F".format(round(main['temp_max']))
        self.low = "{} °F".format(round(main['temp_min']))
        self.condition = conditions[0]['main']
        self.conditionFile = self.displayConditions()
        self.wind = "{} {} mph".format(self.windDirection(), self.windSpeed())
        self.description = conditions[0]['description']
        self.humidity = "{}%".format(main['humidity'])
        self.visibility = self.visibility()

    def displayConditions(self):
        if self.condition == "Clouds":
            return "clouds.gif"
        elif self.condition == "Clear":
            return "sunny.gif"
        elif self.condition == "Rain" or self.condition == "Drizzle" or self.condition == "Mist":
            return "rain.gif"
        elif self.condition == "Thunderstorm":
            return "thunder.gif"
        elif self.condition == "Snow":
            return "snow.gif"
        elif self.condition == "Fog":
            return "fog.gif"
        # add other weather conditions

        # defaults to sun image
        return "sunny.gif"

    def sunrise(self):
        return time.strftime("%I:%M %p", time.localtime(weatherData['sys']['sunrise']))

    def sunset(self):
        return time.strftime("%I:%M %p", time.localtime(weatherData['sys']['sunset']))

    def windSpeed(self):
        return round(weatherData['wind']['speed'])

    def windDirection(self):
        direction = weatherData['wind']['deg']
        if 23 <= direction <= 67 or 293 <= direction <= 337:
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
        else:
            return "N"

    def visibility(self):
        v = weatherData['visibility'] * 0.000621371
        if v < 1:
            v = round(v, 1)
        else:
            v = round(v)
        return "{} mi".format(v)

        # # Weather
        # self.w = weather.Weather()
        # self.tempLabel = tk.Label(master)
        # self.tempLabel.grid(row=4, column=0)
        # self.tempLabel.configure(text=self.w.temp, fg='white', bg='black', font=("Helvetica", 50))
        #
        # self.conditionLabel = tk.Label(master)
        # self.conditionLabel.grid(row=2, column=0)
        # self.conditionLabel.configure(text=self.w.condition, fg='white', bg='black', font=("Helvetica", 50))
        #
        # self.conditionImage = tk.PhotoImage(file=self.w.conditionFile)
        # self.conditionImageLabel = tk.Label(master)
        # self.conditionImageLabel.grid(row=3, column=0)
        # self.conditionImageLabel.configure(image=self.conditionImage, bg='black')
