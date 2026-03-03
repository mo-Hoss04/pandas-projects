import requests
import json
import pandas as pd
import pprint


url = 'https://open.er-api.com/v6/latest/USD'

response = requests.get(url)

data =  response.text

parse = json.loads(data)

list_currencies = parse['rates']

currency_dict = list_currencies.items()

currencylist = []
ratelist = []

for key, value in currency_dict:
    currencylist.append(key)
    ratelist.append(value)


data = {
    "Currency": currencylist,
    "Rate": ratelist
}

df= pd.DataFrame(data)
pd.set_option('display.max_rows', None)
    
print(df)

df.to_csv("USD_exchangerate.csv", index=True)
#print(currency)
