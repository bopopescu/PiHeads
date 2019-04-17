import requests, json

def check_if_home(name):
    SEAN_AIO_KEY = 'aee1d554ecbd4ae28425eb62004f1c24'
    username = 'smcf7'
    group = 'piheads-smart-display'
    seanUrl = 'https://io.adafruit.com/api/v2/{}/groups/{}?X-AIO-Key={}'.format(username, group, SEAN_AIO_KEY)
    samUrl = 'https://io.adafruit.com/api/v2/Zeldatwili/feeds/sam?X-AIO-Key=e546c305d7ef4988867626244f52ce01'
    kyleUrl = 'https://io.adafruit.com/api/v2/Tek5x/feeds/imnotnamingitwhateveriwant?X-AIO-Key=16270dda24cc4cbc91c72154811a5999'

    seanResponse = requests.get(seanUrl)
    seanResponse.raise_for_status()
    samResponse = requests.get(samUrl)
    samResponse.raise_for_status()
    kyleResponse = requests.get(kyleUrl)
    kyleResponse.raise_for_status()

    # Load JSON data into a Python variable
    seanData = json.loads(seanResponse.text)
    samData = json.loads(samResponse.text)
    kyleData = json.loads(kyleResponse.text)

    if name is 'Kyle':
        return "Kyle: {}".format(kyleData['last_value'])
    if name is 'Sam':
        return "Sam: {}".format(samData['last_value'])
    if name is 'Sean':
        return "Sean: {}".format(seanData['feeds'][2]['last_value'])
