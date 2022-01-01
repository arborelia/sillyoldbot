import tweepy
from sillyoldbot.secrets import *

client = tweepy.Client(
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET
)