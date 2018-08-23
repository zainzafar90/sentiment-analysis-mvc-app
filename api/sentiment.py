import twitter_client
import analyzer
import pandas as pd
import numpy as np
import json


class Sentiment():
     def get(self, query):
        tc = twitter_client.TwitterClient()
        tweet_analyzer = analyzer.TweetAnalyzer()
        tweets = tc.get_tweets(query, 10)
        df = tweet_analyzer.tweets_to_data_frame(tweets)
        df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
        return df.to_dict(orient='records'), 200