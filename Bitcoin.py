import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


# Test 1: Check status code is 200
# Test 2: Check that Data object is type json
# Test 3: Check that Data is not empty
def getBitcoindata():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    Data = response.json()
    return Data


# Test 1: Check that currentvalues list is not empty
# Test 2: Check that currentvalues list has 4 elements and not null
# Test 3: Check that time is a date and other 3 vars are ints.
def parseJson(Data):
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
    currentvalues = [time, USD, EURO, GBP]
    return currentvalues


# Test 1: Check that expected print response is recorded
# Test 2: Check that all vars used are not null/empty
def PrintPriceIndex(currentvalues):
    disc = Data['disclaimer']
    crypto = Data['chartName']
    print(f'{disc}')
    print(f'Current price of {crypto} at {currentvalues[0]}:')
    print(f'United States Dollars(USD): ${currentvalues[1]}')
    print(f'Euros(EUR): €{currentvalues[2]}')
    print(f'British pound sterlings(GBP): £{currentvalues[3]}')


# Test 1: Check that dataframe is a 1 row 4 column table
# Test 2: Check that parseJson function has worked and return a list of 4
# values in order
# Test 3: Check that sql database bitcoin exists
# Test 4: Check that table Price_Index in bitcoin is made and not empty
# Test 5: Check that Price_Index table is not overwritten and adds new
# value each call
def addtoPriceIndex():
    col_names = ['Date', 'USD', 'EURO', 'GBP']
    df = pd.DataFrame(columns=col_names)
    df.loc[len(df.index)] = parseJson(Data)
    # print(df)
    engine = create_engine('mysql://root:codio@localhost/bitcoin')
    df.to_sql('Price_Index', con=engine, if_exists='append', index=False)
    return


if __name__ == "__main__":
    Data = getBitcoindata()
    PrintPriceIndex(parseJson(Data))
    addtoPriceIndex()
