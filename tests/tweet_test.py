import unittest
import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from .. import tweet
from tweet import Tweepy

class TweetTest(unittest.TestCase):

    def setUp(self):
        return None

    # @pytest.mark.skip(reason="skip 1")
    def test_max_length_tweet_is_not_int(self):
        max_length_tweet = 'abc'

        with pytest.raises(ValueError):
            t = Tweepy(max_length_tweet=max_length_tweet)

    # @pytest.mark.skip(reason="skip 1")
    def test_max_length_tweet_is_not_less_than_one(self):
        ml_tweet_1 = 0
        ml_tweet_2 = -10

        with pytest.raises(Exception):
            t = Tweepy(max_length_tweet=ml_tweet_1)

        with pytest.raises(Exception):
            t = Tweepy(max_length_tweet=ml_tweet_2)

    def test_clean_text(self):
        assert True

    
    def test_tweet2vec(self):
        random_tweet = "@nothaarsh yeah #probability and all is interesting and fun when you have an urn with 10 blue and 15 red balls!!! #trending"

        t = Tweepy()

        vector = t.tweet2vec(random_tweet)

        self.assertEqual(len(vector), 75)
        
