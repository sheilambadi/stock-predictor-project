import csv
import re
import textblob
from textblob import TextBlob
from setup import *

# list of stocks
# stockTickers = ['#aapl', '#amzn', '#fb', '#gm', '#goog', '#googl', '#msft', '#nflx', '#tsla', '#twtr']
stockTickers = ['#aapl', '#amzn']

def getTweets(searchKey):
    results = filterTweets(searchKey)
    return results

def tweets(search):
    tweetResults = getTweets(search)
    # save reults to csv file
    with open ('Tweets CSV Files/'+str(search)+'.csv', 'a', newline='') as f:
        fieldnames = ['searchKey', 'tweetId', 'tweetDate', 'tweet', 'polarity']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)

        for tweet in tweetResults:
            if not tweet.retweeted and 'RT @' not in tweet.text:
                clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*|(@[A-Za-z0-9]+)', '', tweet.text)
                blob = TextBlob(clean_tweet)
                # analyze
                polarity = blob.sentiment.polarity;
                thewriter.writerow({'searchKey' : str(search), 'tweetId' : tweet.id,'tweetDate': tweet.created_at, 'tweet' : clean_tweet, 'polarity':polarity})

# looping through stock ticker list and averaging tweets
def getTwitterData():
    for ticker in stockTickers:
        tweets(ticker)
        print(ticker + ' saved')
