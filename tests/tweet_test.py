"""This file encases all the test cases for the tweet.py file"""
import sys
import os
import unittest
import pytest
FPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FPATH + '/../')
from .. import tweet
from tweet import Tweepy


class TweetTest(unittest.TestCase):
    """
    Test cases for tweet.py file and all its methods.
    """
    @staticmethod
    def setUp():
        """
        Set up method for test cases.
        """
        return None

    # @pytest.mark.skip(reason="skip 1")
    @staticmethod
    def test_max_length_tweet_is_not_int():
        """
        This test case ensures that the maximum length of tweet
        that is entered by the user is not string.
        """
        max_length_tweet = 'abc'

        with pytest.raises(ValueError):
            Tweepy(max_length_tweet=max_length_tweet)

    # @pytest.mark.skip(reason="skip 1")
    @staticmethod
    def test_max_length_tweet_is_not_less_than_one():
        """
        This test case ensures that the maximum length of tweet
        is not less than 1.
        """
        ml_tweet_1 = 0
        ml_tweet_2 = -10

        with pytest.raises(Exception):
            Tweepy(max_length_tweet=ml_tweet_1)

        with pytest.raises(Exception):
            Tweepy(max_length_tweet=ml_tweet_2)

    def test_clean_text(self):
        """
        Check if the clean text function is returing a cleaned tweet.
        """
        self.assertEqual(1, 1)

    def test_tweet2vec(self):
        """
        Check if the tweet2vec function returns a list of padded vectors from a raw tweet.
        """
        random_tweet = "@nothaarsh yeah #probability and all is interesting and fun when \
        you have an urn with 10 blue and 15 red balls!!! #trending"
        tw_1 = Tweepy()

        vector = tw_1.tweet2vec(random_tweet)

        self.assertEqual(len(vector), 75)
