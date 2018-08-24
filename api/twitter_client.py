from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import authenticator

# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = authenticator.TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_tweets(self, query, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=str(query), tweet_mode="extended").items(num_tweets):
            tweets.append(tweet)
        return tweets