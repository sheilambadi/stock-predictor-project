import pandas as pd 
import datetime

# list of stocks
# stockTickers = ['aapl', 'amzn', 'fb', 'gm', 'goog', 'googl', 'msft', 'nflx', 'tsla', 'twtr']
# only use these 2 tickers to save on streaming time
stockTickers = ['aapl', 'amzn']

def calculate_average(filename):
    # read all stock files where average is to be calculated
    df = pd.read_csv('Tweets CSV Files/#' + filename + '.csv')
    df.columns = ['Ticker', 'id', 'date', 'tweet', 'polarity']
    df['date']= df['date'].apply(pd.to_datetime)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df2 = df.groupby('date')['polarity'].mean().apply(lambda x: '{:.4f}'.format(x))
    df2.to_csv('Average Polarity CSVs/avg_'+filename+'.csv')

    print(df2)

# looping through stock ticker list and saving tweets
def calculateAvgPolarity():
    for ticker in stockTickers:
        calculate_average(ticker)
        print(ticker + ' saved')
