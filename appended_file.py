import pandas as pd
import os

def save_appended_file(ticker):
    # file to save data after appending polarity to stock data
    file_to_save = "stock_polarity_data.csv"
    df_stock = pd.read_csv('Stock CSV Files/stock_market_data-' + ticker.upper() +'.csv')
    df_tweets = pd.read_csv('Average Polarity CSVs/avg_' + ticker + '.csv', names=['Date', 'Polarity'])
    df_stock = df_stock.sort_values('Date', ascending=False)

    # merge the 2 datasets on Date
    new_df = pd.merge(df_stock, df_tweets, on='Date')
    new_df['Ticker'] = ticker.upper()
    # save merged data
    new_df.to_csv(file_to_save, mode = 'a', header=False)

    # append data of the same date together
    # data too few so won't be used in model until it grows significantly
    '''
    sum_file = "stock_polarity_sum_data.csv"
    hybrid_columns = ['Date','Low','High','Close','Open','Volume', 'Adj Close', 'Polarity', 'Ticker']
    # load training data
    df = pd.read_csv('stock_polarity_data.csv', names = hybrid_columns)
    sum_df = df.groupby(['Date', 'Ticker']).mean()
    sum_df.to_csv(sum_file, mode = 'a', header=False)
    '''

# list of stocks
# stockTickers = ['aapl', 'amzn', 'fb', 'gm', 'googl', 'msft', 'nflx', 'tsla', 'twtr']
stockTickers = ['aapl', 'amzn']

# append data for all stock tickers
def appendPolarity():
    for ticker in stockTickers:
        save_appended_file(ticker)
        print(ticker+'appended')