import sys

# secret key protection for git commit
import os  # package that allows to access env. variables
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import json

# import tweepy library
import tweepy

# import textblob library
from textblob import TextBlob

# elk enterprise connection. import elsaticsearch library for python to coonect elasic cloud instance
from elasticsearch import Elasticsearch

import pandas as pd
import re as re

sys.path.append("./environment")
from config import *

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

cloud_id = os.getenv("cloud_id")
user = os.getenv("user")
password = os.getenv("password")

es = Elasticsearch(cloud_id=cloud_id, http_auth=(user, password))

class TweetStreamListener(tweepy.StreamListener):
    def on_data(self, data):

        dict_data = json.loads(data)

        #feature extraction
        df = pd.DataFrame({"tweetTextData": [dict_data["text"]],})

        def search_words(text):
            result = re.findall(r"\b[^\d\W]+\b", text)
            return " ".join(result)

        df["only_words"] = df["tweetTextData"].apply(lambda x: search_words(x))
        tweettext = df["only_words"].values[0]

        #sentiment analysis
        tweet = TextBlob(tweettext)

        print(tweet.sentiment.polarity)

        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "normal"
        else:
            sentiment = "positive"

        print(sentiment)

        es.index(
            index="mappingtestt",
            doc_type="_doc",
            body={
                "author": dict_data["user"]["screen_name"],
                "date": dict_data["created_at"],
                "location": dict_data["user"]["location"],
                "followers": dict_data["user"]["followers_count"],
                "friends": dict_data["user"]["friends_count"],
                "time_zone": dict_data["user"]["time_zone"],
                "lang": dict_data["user"]["lang"],
                "message": dict_data["text"],
                "polarity": tweet.sentiment.polarity,
                "subjectivity": tweet.sentiment.subjectivity,
                "sentiment": sentiment,
                "location2": dict_data["user"]["location"],
                "location":{
                    "lat":41.12,
                    "lon":-71.34
                }

            },
        )
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__": #is used to execute some code only if the file was run directly, and not imported

    listener = TweetStreamListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, listener)
    stream.filter(track=["ukraine"])

