"""This script takes in a tweet and produces a list of vectors (padded)
which can directly be used in a model to provide sentiment analysis."""
import re
import os
import sys
from __init__ import STOPWORDS, EMBEDDINGS, WORD_LIST
from casual import TweetTokenizer

FILEPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FILEPATH + '/')

class Tweepy():
    """
    Tweepy is a class that is used to clean, tokenize and give a list of
    padded vectors from a raw tweet.
    Init parameters:

    :param max_length_dictionary: number of words that should be loaded
    from the embeddings dictionary
    :param max_length_tweet: number of words in a tweet that should be
    considered to produce the output vector
    """
    def __init__(self, max_length_dictionary=len(WORD_LIST), max_length_tweet=75):

        self.stopwords = STOPWORDS
        self.embeddings = EMBEDDINGS
        self.word_list = WORD_LIST

        # check if max lengths are integers and then put an upper limit to it in case of junk value
        if int(max_length_tweet):
            self.max_length_tweet = int(max_length_tweet)
        else:
            raise ValueError

        if int(max_length_dictionary):
            self.max_length_dictionary = int(max_length_dictionary)
            self.word_list = self.word_list[:max_length_dictionary]
        else:
            raise ValueError

        if self.max_length_dictionary < 1 or self.max_length_tweet < 1:
            raise Exception("Max length cannot be less than 1")


    def clean_text(self, tweet):
        """
        Clean the tweet by removing stopwords, numbers, punctuations and other
        characters that won't help in sentiment analysis.

        :param tweet: a unicode string or a byte string encoded in the given
        `encoding` (which defaults to 'utf-8').

        :returns: A clean unicode string.
        """
        tweet_list = tweet.split(" ")

        # Removing twitter handle
        tweet_list = [w for w in tweet_list if not w.startswith("@")]

        tweet = " ".join(tweet_list)

        # removing hashtags from tweet
        tweet = re.sub('#', '', tweet)

        #removing numbers from tweet as they are not present in the embedding dictionary
        tweet = re.sub('[0-9]+', '', tweet)

        # finding all words from the tweet to also get rid of punctuations
        words = re.findall(r'\w+', tweet)

        # Removing stopwords
        for word in words:
            if word in self.stopwords or word.startswith('@'):
                words.remove(word)

        cleaned_tweet = " ".join(words)

        return cleaned_tweet

    @staticmethod
    def tokenize_text(cleaned_tweet):
        """
        Convert the cleaned tweet into a list of tokens using TweetTokenizer (NLTK).

        :param cleaned_tweet: a unicode string or a byte string encoded in the given
        `encoding` returned by the method clean_text.

        :returns: A list of tokens.

        Example:
        s1 = '@remy: This is waaaaayyyy too much for you!!!!!!'
        tknzr.tokenize(s1)
        ['This', 'is', 'waaayyy', 'too', 'much', 'for', 'you']
        """
        tkn = TweetTokenizer()
        tokens = tkn.tokenize(cleaned_tweet)

        return tokens

    def replace_token_with_index(self, token_list):
        """
        Replace the list of tokens with their vectors from the embedding dictionary.

        :param token_list: A list of tokens.

        :returns: A list of vectors for every word (token).
        """
        index_list = []
        for token in token_list:
            try:
                print(self.word_list.index(token))
                index_list.append(self.word_list.index(token))
            except ValueError:
                pass

        return index_list

    def pad_sequence(self, vector_list):
        """
        Add padding to the list of vectors depending on the size of max_length_tweet.

        If the vector is less than the maximum length, add the necessary zero vectors.
        If the vector is more than the maximum length, truncate the list of vectors accordingly.

        :param vector_list: A list of vectors for every token.

        :returns: A padded list of vectors.
        """
        zeroes = [0]
        if len(vector_list) > self.max_length_tweet:
            vector_list = vector_list[:self.max_length_tweet]

        elif len(vector_list) < self.max_length_tweet:
            for _ in range(0, self.max_length_tweet-len(vector_list)):
                vector_list.extend(zeroes)

        else:
            pass

        return vector_list

    def tweet2vec(self, tweet):
        """
        Function that encapsulates all the other functions. It takes in a tweet and outputs the
        list of padded vectors that can directly be used by a model for sentiment analysis.

        :param tweet: a unicode string or a byte string encoded in the given
        `encoding` (which defaults to 'utf-8').

        :returns: A padded list of vectors.
        """
        cleaned_tweet = self.clean_text(tweet)
        tokens = self.tokenize_text(cleaned_tweet)
        index = self.replace_token_with_index(tokens)
        vectors = self.pad_sequence(index)

        return vectors


t = Tweepy(max_length_tweet=30)
z = t.tweet2vec("my name is harsh and i dakjsdsa not a !! dkj @ndka")
print(z)