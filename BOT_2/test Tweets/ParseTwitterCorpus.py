import tweepy
import time
import pickle
import argparse
import re

#partially taken from https://github.com/hongweizeng/Dialogue-Corpus

emoji_pattern = r'/[U0001F601-U0001F64F]/u'

parser = argparse.ArgumentParser(description='distinct-n')

parser.add_argument('-data', type=str, default="twitter_ids.txt",
                    help='Path to the *-train.pt file from preprocess.py')

opt = parser.parse_args()

# insert your own keys
consumer_key = '0UVdW2BXUtNJcQwCq7Tw52Erp'
consumer_secret = 'g9jVPZvfg9ySBdWHb1XKKQ3whnSr1xFLq703ZGYcZqBC31ev1K'
access_token = '2944605422-5bBAKZuOxacXkOi0VbJx6lrlqHvnUmYnM36T1Gx'
access_token_secret = 'HuoJWnpCo7ZRQItTGAfrMpeotYFc1TkRx2hlRrBl5uzGo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


def main():
    twitter_ids_lines = open("TwitterDialogueCorpus/TweetIDs/TweetIDs_Valid_Small.txt", "r").readlines()
    twitter_dlg = open("twitter.dlg.txt", 'w')

    id2text = {}
    index = 0
    for line in twitter_ids_lines:
        id_list = [int(_id) for _id in line.strip().split("\t")]
        for id_ in id_list:

            try:
                result = api.get_status(id_)
                # if(result.lang != 'en'):
                #     continue
                cleanText = re.sub(emoji_pattern, '', result.text)
                cleanText.encode('ascii','ignore').decode('ascii')
                cleanText = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', cleanText, flags=re.MULTILINE)
                cleanText = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",cleanText).split())
                id2text[result.id] = cleanText.encode("utf-8").replace("\n", " ")
                # print(id2text[result.id])
                twitter_dlg.write("%s __eou__ " % id2text[result.id])
                index+=1
            except tweepy.error.TweepError:
                continue
        twitter_dlg.write("\n__eod__\n")
        print("Crawling index ", index)

if __name__ == '__main__':
    main()
