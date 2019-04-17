import requests, json

def check_if_home(name):
    SEAN_AIO_KEY = 'aee1d554ecbd4ae28425eb62004f1c24'
    username = 'smcf7'
    group = 'piheads-smart-display'
    seanUrl = 'https://io.adafruit.com/api/v2/{}/groups/{}?X-AIO-Key={}'.format(username, group, SEAN_AIO_KEY)



    seanResponse = requests.get(seanUrl)
    seanResponse.raise_for_status()

    # Load JSON data into a Python variable
    data = json.loads(seanResponse.text)

    if name is 'Kyle':
        return "{}: {}".format(data['feeds'][0]['name'], data['feeds'][0]['last_value'])
    if name is 'Sam':
        return "{}: {}".format(data['feeds'][1]['name'], data['feeds'][1]['last_value'])
    if name is 'Sean':
        return "{}: {}".format(data['feeds'][2]['name'], data['feeds'][2]['last_value'])
