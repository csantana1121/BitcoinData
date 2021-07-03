import requests
import json
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine


# Test 1: Check status code is 200
# Test 3: Check that Data is not empty
def getBitcoindata():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    return response


def getDatafromlast30days():
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    response = requests.get(url)
    return response


# Test 1: Check that Data object is type json
def convertJson(response):
    return response.json()


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


def parsehistJson(Data):
    disc = Data['disclaimer']
    USD = Data['bpi']
    return USD


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
# option= append: to add at the end of the table
# replace: to wipe the table clean and restart collecting new data
def addtoPriceIndex(option):
    col_names = ['Date', 'USD', 'EURO', 'GBP']
    df = pd.DataFrame(columns=col_names)
    df.loc[len(df.index)] = parseJson(Data)
    # print(df)
    engine = create_engine('mysql://root:codio@localhost/bitcoin')
    df.to_sql('Price_Index', con=engine, if_exists=option, index=False)
    return


def addtoHistPriceIndex():
    col_names = ['Day', 'USD']
    items = parsehistJson(Data)
    df = pd.DataFrame(columns=col_names)
    for key, value in items.items():
        df.loc[len(df.index)] = [key, value]
    # print(df)
    engine = create_engine('mysql://root:codio@localhost/bitcoin')
    df.to_sql('Hist_Price_Index', con=engine, if_exists='replace', index=False)


def loadSQLfromFile(filename, database_name):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + database_name + '; "')
    os.system("mysql -u root -pcodio " + database_name + " < " + filename)


def saveSQLtofile(filename, database_name):
    os.system("mysqldump -u root -pcodio " + database_name + " > " + filename)


def plotData(database_name, table_name, filename):
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    fig, ax = plt.subplots()
    if table_name == 'Hist_Price_Index':
        ax.plot(df['Day'], df['USD'], label='USD')
        ax.set_xlabel('Day')
        ax.set_ylabel('price')
        ax.set_title('Bitcoin Historical Price_Index')
        ax.legend()
        plt.show()
    else:
        USD = df['USD']
        dollar = []
        EURO = df['EURO']
        euros = []
        GBP = df['GBP']
        pounds = []
        time = df['Date']
        for value in USD:
            temp = float(value.replace(',', ''))
            dollar.append(temp)
        for value in EURO:
            temp = float(value.replace(',', ''))
            euros.append(temp)
        for value in GBP:
            temp = float(value.replace(',', ''))
            pounds.append(temp)
        ax.plot(time, pounds, label='GBP')
        ax.plot(time, euros, label='EURO')
        ax.plot(time, dollar, label='USD')
        ax.set_xlabel('time')
        ax.set_ylabel('price')
        ax.set_title('Bitcoin Price_Index')
        ax.legend()
        plt.show()


def createEngine(database_name):
    return create_engine('mysql://root:codio@localhost/' + 'bitcoin')


if __name__ == "__main__":
    loadSQLfromFile('bitcoin.sql', 'bitcoin')
    response = getBitcoindata()
    Data = convertJson(response)
    ParseData = parseJson(Data)
    PrintPriceIndex(ParseData)
    addtoPriceIndex('append')
    Data = convertJson(getDatafromlast30days())
    addtoHistPriceIndex()
    saveSQLtofile('bitcoin.sql', 'bitcoin')
    plotData('bitcoin', 'Hist_Price_Index', 'bitcoin.sql')
    plotData('bitcoin', 'Price_Index', 'bitcoin.sql')
