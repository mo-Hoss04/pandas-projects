import requests
import json

url = "https://api.coinbase.com/v2/currencies"

response = requests.get(url)

data = response.text

parse = json.loads(data)

list_currencies = parse['data']

search  = input("Enter Currency ID: ")

for i in list_currencies:
    if search == i['id']:
        print(i['name'])

    



