#get sentence structure
#use n grams to develop newer sentence structure
import tweepy
from textblob import TextBlob
import re
import sys

emoji_pattern = r'/[U0001F601-U0001F64F]/u'

consumer_key = '0UVdW2BXUtNJcQwCq7Tw52Erp'
consumer_secret = 'g9jVPZvfg9ySBdWHb1XKKQ3whnSr1xFLq703ZGYcZqBC31ev1K'
access_token = '2944605422-5bBAKZuOxacXkOi0VbJx6lrlqHvnUmYnM36T1Gx'
access_token_secret = 'HuoJWnpCo7ZRQItTGAfrMpeotYFc1TkRx2hlRrBl5uzGo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

CC	= []
CD	= []
DT  = []
EX	= []
FW	= []
IN	= []
JJ	= []
JJR	= []
JJS	= []
LS  = []
MD	= []
NN	= []
NNS	= []
NNP	= []
NNPS= []
PDT	= []
POS	= []
PRP	= []
PRPD = []
RB	= []
RBR	= []
RBS	= []
RP	= []
TO	= []
UH	= []
VB  = []
VBD	= []
VBG	= []
VBN	= []
VBP	= []
VBZ	= []
WDT	= []
WP	= []
WPD	= []
WRB	= []


templates = []

def updateDict(postag):
    for i in postag:
        if(i[1] == 'CC'):
            CC.append(i[0])
        elif(i[1] == 'CD'):
            CD.append(i[0])
        elif(i[1] == 'DT'):
            DT.append(i[0])
        elif(i[1] == 'EX'):
            EX.append(i[0])
        elif(i[1] == 'FW'):
            FW.append(i[0])
        elif(i[1] == 'IN'):
            IN.append(i[0])
        elif(i[1] == 'JJ'):
            JJ.append(i[0])
        elif(i[1] == 'JJR'):
            JJR.append(i[0])
        elif(i[1] == 'JJS'):
            JJS.append(i[0])
        elif(i[1] == 'LS'):
            LS.append(i[0])
        elif(i[1] == 'MD'):
            MD.append(i[0])
        elif(i[1] == 'NN'):
            NN.append(i[0])
        elif(i[1] == 'NNS'):
            NNS.append(i[0])
        elif(i[1] == 'NNP'):
            NNP.append(i[0])
        elif(i[1] == 'NNPS'):
            NNPS.append(i[0])
        elif(i[1] == 'PDT'):
            PDT.append(i[0])
        elif(i[1] == 'POS'):
            POS.append(i[0])
        elif(i[1] == 'PRP'):
            PRP.append(i[0])
        elif(i[1] == 'PRP$'):
            PRPD.append(i[0])
        elif(i[1] == 'RB'):
            RB.append(i[0])
        elif(i[1] == 'RBR'):
            RBR.append(i[0])
        elif(i[1] == 'RBS'):
            RBS.append(i[0])
        elif(i[1] == 'RP'):
            RP.append(i[0])
        elif(i[1] == 'TO'):
            TO.append(i[0])
        elif(i[1] == 'UH'):
            UH.append(i[0])
        elif(i[1] == 'VB'):
            VB.append(i[0])
        elif(i[1] == 'VBD'):
            VBD.append(i[0])
        elif(i[1] == 'VBN'):
            VBN.append(i[0])
        elif(i[1] == 'VBP'):
            VBP.append(i[0])
        elif(i[1] == 'VBZ'):
            VBZ.append(i[0])
        elif(i[1] == 'VBG'):
            VBG.append(i[0])
        elif(i[1] == 'WDT'):
            WDT.append(i[0])
        elif(i[1] == 'WP'):
            WP.append(i[0])
        elif(i[1] == 'WP$'):
            WPD.append(i[0])
        elif(i[1] == 'WRB'):
            WRB.append(i[0])


def sentencePos(text):
    blob = TextBlob(text)
    sentence_pos = []
    for pos in blob.tags:
        sentence_pos.append(pos)
    return sentence_pos

def genTemplate(keyword):
    for i in range(1):
        public_tweets = api.search(q = keyword,
                                   count = 100,
                                   lang = 'en')
        for tweet in public_tweets:
            grammar = []
            cleanText = re.sub(emoji_pattern, '', tweet.text)
            cleanText.encode('ascii', 'ignore').decode('ascii')
            cleanText = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', cleanText, flags=re.MULTILINE)
            cleanText = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cleanText).split())
            postag = sentencePos(cleanText)
            for i in range(len(postag)):
                grammar.append(postag[i][1])
            templates.append(grammar)
            updateDict(postag)



#https://github.com/errollw/gengram

# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'
# POS	possessive ending	parent's
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when