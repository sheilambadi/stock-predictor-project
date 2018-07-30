import pandas as pd 
import datetime

def calculate_average(filename, ticker):
    df = pd.read_csv(filename)
    df.columns = ['Ticker', 'id', 'date', 'tweet', 'polarity']
    df['date']= df['date'].apply(pd.to_datetime)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    df2 = df.groupby('date')['polarity'].mean().apply(lambda x: '{:.4f}'.format(x))
    df2.to_csv('Average Polarity CSVs/avg_'+ticker+'.csv')

    print(df2)

calculate_average('Tweets CSV Files/'+'#nflx.csv', 'nflx')