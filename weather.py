import requests, json

# Download json data
url = 'http://api.openweathermap.org/data/2.5/weather?id=4846834&APPID=f48818a446c345dfa46a2222c9fa1acf&units=imperial'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['main']
print(f"Temperature: {w['temp']} °F")
print(f"High: {w['temp_max']} °F")
print(f"Low: {w['temp_min']} °F")
