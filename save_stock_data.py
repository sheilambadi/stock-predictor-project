import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data
import datetime as dt
import urllib.request, json
import numpy as np

def saveStockDate(ticker):
    # alpha vantage api key
    api_key = '6BXJN99BEYM5VWU3'

    # JSON file with all the stock market data for AMZN from the last 20 years
    url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=full&apikey=%s"%(ticker,api_key)

    # Save data to this file
    file_to_save = 'Stock CSV Files/stock_market_data-%s.csv'%ticker

    # Saved data,
    # Grab the data from the url
    # And store date, low, high, volume, close, open, adj close values to a Pandas DataFrame
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
        # extract stock market data
        data = data['Time Series (Daily)']
        df = pd.DataFrame(columns=['Date','Low','High','Close','Open','Volume', 'Adj Close'])
        for k,v in data.items():
            date = dt.datetime.strptime(k, '%Y-%m-%d')
            data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                        float(v['4. close']),float(v['1. open']),float(v['6. volume']),float(v['5. adjusted close'])]
            df.loc[-1,:] = data_row
            df.index = df.index + 1
    print('Data saved to : %s'%file_to_save)        
    df.to_csv(file_to_save, mode='a', header=False)
    return df


# list of stocks
stockTickers = ['AAPL', 'AMZN']
# stockTickers = ['AAPL', 'AMZN', 'FB', 'GM', 'GOOG', 'GOOGL', 'MSFT', 'NFLX', 'TSLA', 'TWTR']

# Amazon stock market prices
def getStockData():
    for stock in stockTickers:
        saveStockDate(stock)
