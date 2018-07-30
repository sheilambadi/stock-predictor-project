from credentials import *
import tweepy

# APIs Setup
def twitterSetup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Return API with authentication
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
    
def filterTweets(searchClause):
    # Create a tweet extractor object
    extractor = twitterSetup()
    # Create a tweet item iterator filtered by search clause
    tweets = tweepy.Cursor(extractor.search, q=searchClause).items()

    return tweets
