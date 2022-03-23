import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = "AU7Ma83BEiaA7GdF3l9D9tYUf" 
api_key_secret = "miQyH7ueEiwEIu7i0989MElgAmibfP99tyPHRIO6O6PI97mkdR" 

access_token = "1374444599461113862-2XWdvEPY89FtsnGMLY2E12I9VWtD8c"   
access_token_secret = "XwIdWhZFXT8eqYAttgxv1mZwvWoZsaxdQ2AX2VIZCziEs" 

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
user = 'en_esittir_tr'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)