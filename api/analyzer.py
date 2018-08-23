from textblob import TextBlob
import re
import pandas as pd
import numpy as np
import time


class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_formatted_date_time(self, datetime):
        return  time.strftime('%H:%M %p - %b %d %Y', time.strptime(str(datetime), '%Y-%m-%d %H:%M:%S'))

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1
    
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['text'] = np.array([tweet.text for tweet in tweets])
        print df['text']
        df['name'] = np.array([tweet.user.name for tweet in tweets])
        df['screen_name'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['profile_image_url'] = np.array([tweet.user.profile_image_url for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([self.get_formatted_date_time(tweet.created_at) for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        
        return df
