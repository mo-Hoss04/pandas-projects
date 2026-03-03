import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')

# Pulling the data from the mentioned API
data = response_API.text

# Parsing the data into JSON format
parse =  json.loads(data)

active_cases = parse['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
print("Active cases in South Andaman:", active_cases)