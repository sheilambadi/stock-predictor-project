import pandas as pd
import os

# combine polarity to stock data
# new_df.columns = ['Date','Low','High','Close','Open','Volume', 'Adj Close', 'Date', 'Polarity']
def save_appended_file(ticker):
    file_to_save = "stock_polarity_data.csv"
    df_stock = pd.read_csv('Stock CSV Files/stock_market_data-' + ticker.upper() +'.csv')
    df_tweets = pd.read_csv('Average Polarity CSVs/avg_' + ticker + '.csv', names=['Date', 'Polarity'])
    df_stock = df_stock.sort_values('Date', ascending=False)

    new_df = pd.merge(df_stock, df_tweets, on='Date')
    new_df['Ticker'] = ticker.upper()
    new_df.to_csv(file_to_save, mode = 'a', header=False)

# list of stocks
stockTickers = ['aapl', 'amzn', 'fb', 'gm', 'googl', 'msft', 'nflx', 'tsla', 'twtr']
for ticker in stockTickers:
    save_appended_file(ticker)