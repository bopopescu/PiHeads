import requests
import json
import time

APP_ID = "f48818a446c345dfa46a2222c9fa1acf"

class Weather:
    def __init__(self):
        weatherUrl = 'http://api.openweathermap.org/data/2.5/weather?id=4846834&APPID={}&units=imperial'.format(APP_ID)
        response = requests.get(weatherUrl)
        response.raise_for_status()
        self.weatherData = json.loads(response.text)
        self.main = self.weatherData['main']
        self.conditions = self.weatherData['weather']

        self.temp = "{} °F".format(round(self.main['temp']))
        self.high = "{} °F".format(round(self.main['temp_max']))
        self.low = "{} °F".format(round(self.main['temp_min']))
        self.condition = self.conditions[0]['main']
        self.conditionFile = self.displayConditions()
        self.wind = "{} {} mph".format(self.windDirection(), self.windSpeed())
        self.description = self.conditions[0]['description']
        self.humidity = "{}%".format(self.main['humidity'])
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
        return time.strftime("%I:%M %p", time.localtime(self.weatherData['sys']['sunrise']))

    def sunset(self):
        return time.strftime("%I:%M %p", time.localtime(self.weatherData['sys']['sunset']))

    def windSpeed(self):
        return round(self.weatherData['wind']['speed'])

    def windDirection(self):
        direction = self.weatherData['wind']['deg']
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
        v = self.weatherData['visibility'] * 0.000621371
        if v < 1:
            v = round(v, 1)
        else:
            v = round(v)
        return "{} mi".format(v)

class Forecast:
    def __init__(self):
        forecastUrl = 'http://api.openweathermap.org/data/2.5/forecast?id=4846834&APPID={}&units=imperial'\
            .format(APP_ID)
        response1 = requests.get(forecastUrl)
        response1.raise_for_status()
        self.forecastData = json.loads(response1.text)

    def getForecast(self):
        day = {'name': '', 'high': 0, 'low': 0}
        out = {'day1': day.copy(), 'day2': day.copy(), 'day3': day.copy(), 'day4': day.copy()}
        lastDay = time.strftime("%a", time.localtime(self.forecastData['list'][0]['dt']))
        j = 0
        dayNum = 0

        for i in self.forecastData['list']:
            currDay = time.strftime("%a", time.localtime(i['dt']))

            if lastDay not in currDay and j < 32:
                dayNum += 1
                out['day{}'.format(dayNum)]['name'] = currDay
                out['day{}'.format(dayNum)]['high'], out['day{}'.format(dayNum)]['low'] = self.getHighLow(j)
                lastDay = time.strftime("%a", time.localtime(self.forecastData['list'][j]['dt']))

                if dayNum is 4:
                    return out
            j += 1

    def getHighLow(self, start):
        i = start
        min = self.forecastData['list'][i]['main']['temp_min']
        max = self.forecastData['list'][i]['main']['temp_min']
        while i < (start + 8):
            if self.forecastData['list'][i]['main']['temp_min'] < min:
                min = self.forecastData['list'][i]['main']['temp_min']
            if self.forecastData['list'][i]['main']['temp_max'] > max:
                max = self.forecastData['list'][i]['main']['temp_max']

            i += 1

        return round(max), round(min)
