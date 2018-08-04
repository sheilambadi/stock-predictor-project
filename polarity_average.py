import pandas as pd 
import datetime

# list of stocks
stockTickers = ['#aapl', '#amzn', '#fb', '#gm', '#goog', '#googl', '#msft', '#nflx', '#tsla', '#twtr']

def calculate_average(filename):
    df = pd.read_csv(filename)
    df.columns = ['Ticker', 'id', 'date', 'tweet', 'polarity']
    df['date']= df['date'].apply(pd.to_datetime)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df2 = df.groupby('date')['polarity'].mean().apply(lambda x: '{:.4f}'.format(x))
    df2.to_csv('Average Polarity CSVs/avg_'+filename+'.csv')

    print(df2)

# looping through stock ticker list and saving tweets
for ticker in stockTickers:
    calculate_average('Tweets CSV Files/' + ticker)
    print(ticker + ' saved')
