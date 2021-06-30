import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
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
Pounds = cur['GBP']
GBP = Pounds['rate']

# print(f'{disc}')
# print(f'Current price of {crypto} at {time}:')
# print(f'United States Dollars(USD): ${USD}')
# print(f'Euros(EUR): €{EURO}')
# print(f'British pound sterlings(GBP): £{GBP}')

col_names = ['Date', 'USD', 'EURO', 'GBP']
df = pd.DataFrame(columns=col_names)
df.loc[len(df.index)] = [time, USD, EURO, GBP]
# print(df)
engine = create_engine('mysql://root:codio@localhost/bitcoin')
df.to_sql('Price_Index', con=engine, if_exists='append', index=False)
