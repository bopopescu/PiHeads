import requests, json

def check_if_home():
    AIO_KEY = 'aee1d554ecbd4ae28425eb62004f1c24'
    username = 'smcf7'
    url = 'https://io.adafruit.com/api/v2/{}/feeds?X-AIO-Key={}'.format(username, AIO_KEY)

    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable
    data = json.loads(response.text)
    location = data[1].get('last_value')

    return location
