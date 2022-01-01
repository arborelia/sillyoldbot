import json
from sillyoldbot.auth import client
from sillyoldbot.whereami import data_path

__version__ = "0.1.0"


def get_tweets():
    text = data_path("tweet-sized-pooh.txt").open().read()
    tweets = text.split("\n-\n")
    return tweets


def get_data():
    return json.load(data_path("status.json").open())


def write_data(data):
    out = data_path("status.json").open('w')
    out.write(json.dumps(data))
    out.close()


def run():
    data = get_data()
    tweets = get_tweets()
    tweet = tweets[data["current"]]
    print(tweet)
    client.create_tweet(text=tweet)
    data["current"] += 1
    data["last_tweet"] = tweet
    write_data(data)


if __name__ == "__main__":
    run()
