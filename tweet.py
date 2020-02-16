import re
# import sys
from casual import TweetTokenizer
from .. import STOPWORDS, EMBEDDINGS

class Tweepy():

    def __init__(self, max_length_dictionary=len(EMBEDDINGS), max_length_tweet=75):

        # check if max lengths are integers and then put an upper limit to it in case of junk value
        if int(max_length_tweet):
            self.max_length_tweet = int(max_length_tweet)
        else:
            raise ValueError
        
        if int(max_length_dictionary):
            self.max_length_dictionary = int(max_length_dictionary)
        else:
            raise ValueError

        if self.max_length_dictionary < 1 or self.max_length_tweet < 1:
            raise Exception("Max length cannot be less than 1")

        self.stopwords = STOPWORDS
        self.embeddings = EMBEDDINGS


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
        for w in words:
            if w in self.stopwords or w.startswith('@'):
                words.remove(w)
                
        cleaned_tweet = " ".join(words)

        return cleaned_tweet

    def tokenize_text(self, cleaned_tweet):
        """
        Convert the cleaned tweet into a list of tokens using TweetTokenizer (NLTK).

        :param cleaned_tweet: a unicode string or a byte string encoded in the given
        `encoding` returned by the method clean_text.

        :returns: A list of tokens.

        Example:
            >>> s1 = '@remy: This is waaaaayyyy too much for you!!!!!!'
            >>> tknzr.tokenize(s1)
            ['This', 'is', 'waaayyy', 'too', 'much', 'for', 'you']  
        """
        tkn = TweetTokenizer()
        tokens = tkn.tokenize(cleaned_tweet)
    
        return tokens

    def replace_token_with_index(self, token_list):
        index_list = []
        for token in token_list:
            if self.embeddings.get(token):
                index_list.append(self.embeddings[token])

        return index_list

    def pad_sequence(self, vector_list):
        zeroes = [0] * 25
        if len(vector_list) > self.max_length_tweet:
            vector_list = vector_list[:self.max_length_tweet]

        elif len(vector_list) < self.max_length_tweet:
            for _ in range(0, self.max_length_tweet-len(vector_list)):
                vector_list.append(zeroes)

        else:
            pass

        return vector_list
            
    def tweet2vec(self, tweet):
        cleaned_tweet = self.clean_text(tweet)
        tokens = self.tokenize_text(cleaned_tweet)
        index = self.replace_token_with_index(tokens)
        vectors = self.pad_sequence(index)

        return vectors
