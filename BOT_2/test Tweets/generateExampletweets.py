import tweepy
import re

consumer_key = '0UVdW2BXUtNJcQwCq7Tw52Erp'
consumer_secret = 'g9jVPZvfg9ySBdWHb1XKKQ3whnSr1xFLq703ZGYcZqBC31ev1K'
access_token = '2944605422-5bBAKZuOxacXkOi0VbJx6lrlqHvnUmYnM36T1Gx'
access_secret = 'HuoJWnpCo7ZRQItTGAfrMpeotYFc1TkRx2hlRrBl5uzGo'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)


emoji_pattern = r'/[U0001F601-U0001F64F]/u'

results = api.search(q="NBA AND Warriors AND win", lang='en', count=200, tweet_mode='extended')

sinceid = 0
cleaned_tweets = []

def get_min_id(public_tweets):
    ids = []
    for tweet in public_tweets:
        ids.append(tweet.id)
    if not ids:
        return 0
    else:
        return min(ids)

for i in range(750):
    total_tweets = []

    results = api.search(q="NBA AND Warriors", lang='en', count=200, since_id = sinceid, tweet_mode='extended')
    for tweet in results:
        total_tweets.append(tweet)
        if (not tweet.retweeted) and ('RT' not in tweet.full_text):
            try:
                cleanText = re.sub(emoji_pattern, '', tweet.full_text)
                cleanText.encode('ascii','ignore').decode('ascii')
                cleanText = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', cleanText, flags=re.MULTILINE)
                cleanText = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",cleanText).split())
                if(len(cleanText) < 300 and cleaned_tweets.count(cleanText) <= 5):
                    cleaned_tweets.append(cleanText)

            except:
                    continue
    sinceid = get_min_id(total_tweets)
    print(sinceid, " ", i)


f = open('tweets.txt',"w+")

for i in range(len(cleaned_tweets)):
    f.write(cleaned_tweets[i])
    f.write('\n')

f.close()
