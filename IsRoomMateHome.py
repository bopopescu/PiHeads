import requests

r = requests.post('https://io.adafruit.com/api/v2/webhooks/feed/7zhk7o45zkqJyV66EsRhDE5C95Ys', data = "Yeet")
q = requests.get('https://io.adafruit.com/api/v2/webhooks/feed/7zhk7o45zkqJyV66EsRhDE5C95Ys')
print(q)
