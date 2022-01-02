from sillyoldbot import get_tweets, get_data


def test_status():
    status = get_data()
    assert isinstance(status["current"], int)


def test_tweets():
    tweets = get_tweets()
    assert len(tweets) > 100
    for tweet in tweets:
        assert len(tweet) <= 280, tweet
