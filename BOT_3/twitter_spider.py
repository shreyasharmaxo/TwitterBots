# -*- coding: utf-8 -*-
import tweepy
import time
import pickle
import argparse

#partially taken from https://github.com/hongweizeng/Dialogue-Corpus

parser = argparse.ArgumentParser(description='distinct-n')

parser.add_argument('-data', type=str, default="twitter_ids.txt",
                    help='Path to the *-train.pt file from preprocess.py')

opt = parser.parse_args()

# insert your own keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def main():
    twitter_ids_lines = open(opt.data, "r").readlines()
    twitter_dlg = open("twitter.dlg.txt", 'w')    

    id2text = {}
    id_list = []
    index = 0
    for line in twitter_ids_lines:
        id_list = [int(_id) for _id in line.strip().split("\t")]
        try:
            results = api.statuses_lookup(id_list)
            for result in results:
                id2text[result.id] = result.text.encode("utf-8").replace("\n", " ")
                twitter_dlg.write("%s __eou__ " % id2text[result.id])
            index+=1
            twitter_dlg.write("\n__eod__\n")
        except:
            continue
        if index % 10 == 0:
            print("Crawling index ", index)
            time.sleep(5)
        if index % 100 == 0:
            time.sleep(120)
         
if __name__ == '__main__':
    main()
