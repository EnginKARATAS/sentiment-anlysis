import tweepy
import json


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        place = tweet["place"]
        favorite_count = tweet["favorite_count"]
        retweet_count = tweet["retweet_count"]
        entities = tweet["entities"]
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {
            "created_at": created_at,
            "id_str": id_str,
            "text": text,
            "place": place,
            "favorite_count": favorite_count,
            "retweet_count": retweet_count,
            "entities": entities,
        }
        with app.app_context():
            user = mongo.db.precog_collection
            user.insert(obj)
            print obj

    def on_status(self, status):
        print (status.text)

    def on_error(self, status):
        print status


l = MyStreamListener()
auth = tweepy.OAuthHandler(
    "NjVpbaZxAWauLfVGld9BgbA74", "28LIJ6e8TEZrk6zbOAJYmzl1R1OgyS9G7AZi3o327GFFSoKPzT"
)
auth.set_access_token(
    "704716007361933313-JVGIWW87KFcBAABC7x0vlasER1iFCmh",
    "IFbuxyCDRqzCn8G61LfOZMg8hsDMzVAjhB1zNif1sWZzU",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)
auth = tweepy.OAuthHandler(
    "THqou4VvE8HVeHICMR9UUqwmF", "NdAgLV7QHafZzLQxNCyUw1um53gvlnY7H2qNLMQoqCoAynlxSZ"
)
auth.set_access_token(
    "704716007361933313-OVca5afGxzHIYnD8ts4OlkxIod8SvUf",
    "Zs9GR3DonuL2YWa9XyG0hgKXA6cz8v7IXVKmmsSPuf0K2",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

auth = tweepy.OAuthHandler(
    "2qcxfpQ9SIGtNjzipiu9VaN6v", "otMPyEONy7IsY3ChXQwBMPqmeALh7mQ5rnwZE4f4pm34kja2Q0"
)
auth.set_access_token(
    "704716007361933313-KAHtFIuWxbRMMYNLjiYhIbEt2YOhtwr",
    "PSKMjW1aMknuLXAJM7eg4YcpAktGYMXrWPPSBhPkB4IZr",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

auth = tweepy.OAuthHandler(
    "Dvl5Vu3aLGXY3tzdKp29jf880", "7gcvDtLpx00fFrp1YNCIiXBernhRCpspkYoOvEPZeUFtx52X6q"
)
auth.set_access_token(
    "704716007361933313-O8IERwYbiGv4aoWNkKtj1iYAsDGYv7d",
    "OeNP2n61FYUspTJ0GEynoYKkzgKrcJMDGVXN4efogHlri",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

auth = tweepy.OAuthHandler(
    "JQlgJTMYKpdglVF61wxvnRnOW", "YYgmxAC5hnLUPxqcpK2ozZLxsCcAqJ3UXi4UiklgezZePrBxa8"
)
auth.set_access_token(
    "704716007361933313-3LwMDIW7HppuZ2ixHNqoRV0BKBTJ7Jd",
    "p6E7mspRWZ0nugJ2jXMCJOV41bU608QQeWtNsWcrvWEN3",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

auth = tweepy.OAuthHandler(
    "qjoDXMpyuzy3cKv0ErS8sXURv", "wH8kTWmk80EOw5skiSXPvT3cma3CLrO9kxZr4Wpu1s2qt9Gy7d"
)
auth.set_access_token(
    "704716007361933313-Kw4hXQIiGYK8jHcJ1W79M8nmAFDhvHT",
    "GJRz7k3QBgMLrzywIHQlY0xq44vL3MKZeHL6LcF6S6Kkq",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

auth = tweepy.OAuthHandler(
    "iQyZZOanCHWoy2ElyO8T5XoVu", "xEyJEJeMpV24ay2TmFTIFY5rRKacb6nDuY1GQsyLG0vjhsbnQw"
)
auth.set_access_token(
    "792683109468733440-g3YcTZ9yc7SQ8JxPyrvH6JlojWfY2dA",
    "gBukbtupIFUMZAOYcyYIxdd3oPMFTQd547V9PyG3rnZUa",
)
api = tweepy.API(auth)
myStream = tweepy.Stream(auth=api.auth, listener=l)
myStream.filter(
    track=["donald trump", "trump", "clinton", "hillary clinton"], async=True
)

if __name__ == "__main__":
    app.run(debug=True)
