import requests
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

response = requests.get(url)

Data = response.json()
disc = Data['disclaimer']
crypto = Data['chartName']
times = Data['time']
time = times['updated']
cur = Data['bpi']
USDollar = cur['USD']
USD = USDollar['rate']
EUR = cur['EUR']
EURO = EUR['rate']
print(f'{disc}')
print(f'Current price of {crypto} at {time}:')
print(f'United States Dollars(USD): ${USD}')
print(f'Euros(EUR): €{EURO}')