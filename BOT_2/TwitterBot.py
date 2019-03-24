import tweepy
from random import randint
import time
from TwitterResponse import Response

class TwitterBot:

    def __init__ (self, api):
        self.api = api

    def tweet(self):
        num = randint(0,4)
        tweets = ['Test1','Test2','Test3','Test4','Test5']
        try:
            api.update_status(tweets[num])
        except tweey.error.TweepError:
            print "error" + str(num)


    def favorite_tweet(self):
        home_timeline = api.home_timeline()
        tweet_ids = []
        for i in home_timeline:
            tweet_ids.append(i.id)

        favoriteInt = randint(0,len(tweet_ids)-1)
        api.create_favorite(tweet_ids[favoriteInt])
        print api.favorites()[0].text

    def retweet(self):
        home_timeline = api.home_timeline()
        tweet_ids = []
        for i in home_timeline:
            tweet_ids.append(i.id)

        favoriteInt = randint(0,len(tweet_ids)-1)
        api.retweet(tweet_ids[favoriteInt])
        print "Retweeted: " + str(tweet_ids[favoriteInt])

    def reply_tweet(self):
        home_timeline = api.home_timeline()
        tweet_ids = []
        for i in home_timeline:
            tweet_ids.append(i.id)

        result = Response(tweet_ids['text'],api)
        response = result.getnerateResponse()
        api.update_status(response,tweet_ids[replyInt])

if __name__ == "__main__":

    consumer_key = '0UVdW2BXUtNJcQwCq7Tw52Erp'
    consumer_secret = 'g9jVPZvfg9ySBdWHb1XKKQ3whnSr1xFLq703ZGYcZqBC31ev1K'
    access_token = '2944605422-5bBAKZuOxacXkOi0VbJx6lrlqHvnUmYnM36T1Gx'
    access_secret = 'HuoJWnpCo7ZRQItTGAfrMpeotYFc1TkRx2hlRrBl5uzGo'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)


    bot1 = TwitterBot(api)

    bot1.reply_tweet()
    bot1.favorite_tweet()
    bot1.retweet()
    bot1.tweet()
